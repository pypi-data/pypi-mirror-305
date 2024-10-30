import math
import ollama
from chatollama import ChatEngine, ChatMessages
import inspect
import json
import ast
import re
import os


class ChatTool:
    def __init__(self, callback):
        if not callable(callback):
            raise ValueError(f"'callback' argument should be a function. '{
                             type(callback)}' was passed in")

        self.callback = callback
        self.name, self.header, self.description = self.extract_function_info(
            callback)

    @classmethod
    def extract_function_info(cls, func):
        """
        Extracts the function name, header (signature), and docstring.

        :param func: Function whose information is to be extracted
        :returns: Tuple containing function name, header, and description
        """
        name = func.__name__
        header = f"{name}{inspect.signature(func)}"
        description = inspect.getdoc(func) or ""
        return name, header, description


class ChatToolKit:
    def __init__(self, tools: list[ChatTool] = []):
        self.tools: list[ChatTool] = []
        for tool in tools:
            self.add(tool)
        self.indent: int = 4

    def add(self, tool: ChatTool):
        if isinstance(tool, ChatTool):
            self.tools.append(tool)
        else:
            self.tools.append(ChatTool(tool))

    def get(self, func_name: str):
        for tool in self.tools:
            if tool.name == func_name:
                return tool

    def __str__(self):
        tools = []
        for tool in self.tools:
            tools.append(
                {
                    "function": tool.header,
                    "description": tool.description
                }
            )
        return json.dumps(tools, indent=self.indent)

    def system_prompt(self):
        return f"The following are available tools/functions you have access to:\n\n{self.__str__()}\n\nPlease use them to assist the user. The tools/functions may provide you with information or run actions on the users computer.\n\nPlease use the following format when calling one of the available tools/functions:\n\n```tool\nfunc1(arg1, arg2...)\n```\n\nAlways use full triple backticks and the word tool when making a function call—avoid single backticks or variations. Avoid referencing the use of tools/functions explicitly. Simply execute them within the response to maintain a smooth, unobtrusive interaction. Make sure not to hallucinate any tools. The only tools available to you are the ones listed here"


class ChainEngine(ChatEngine):
    def __init__(self, model="llama3.1:8b", toolkit: ChatToolKit = ChatToolKit()):
        super().__init__(model)
        self.toolkit = toolkit
        self.apply_default_system_prompt()
        self.init_values()

    # Init Functions

    def init_values(self):
        self.callback = self.handle_response
        self.tool_calls = []
        self.append_response_to_messages = False

    # Event Functions

    def chain(self, message: str):
        self.messages.user(message)
        for i in range(10):
            self.tool_calls = []
            self.chat()
            self.wait()
            self.messages.assistant(self.response)
            if len(self.tool_calls) > 0:
                try:
                    parsed_calls = self.parse_function_calls(self.tool_calls)
                    first = parsed_calls[0]
                    func_name = first.get("name")
                    args = first.get("args")
                    kwargs = first.get("kwargs")
                    tool = self.toolkit.get(func_name)
                    if tool == None:
                        self.messages.user(
                            f"<system> This is an automated hidden message from the system, the tool call attempted to be used '{func_name}' does not exist as part of the available tools. Please use an available tool or report to the user that the tool did not work <system>")
                    else:
                        result = tool.callback(*args, **kwargs)
                        self.messages.user(
                            f"<system> This is an automated hidden message from the system, The current used tool returned this\n\n---\n\n{str(result)}\n\n---\n\nPlease continue your response from where you left off for a seamless response. Do not reference this message to the user, simply use the result to give the correct response you had intended before the tool was called. <system>")
                except:
                    self.messages.user(
                        f"<system> This is an automated hidden message from the system, a syntax error occured when parsing the tool call, please correct the call or report to the user the issue and ask how to move forward <system>")

            else:
                break

    def handle_response(self, mode: int, delta: str, text: str):
        if mode == 0:
            print("[AI]:")
        elif mode == 1:
            print(delta, end="")
            if "```" in text:
                try:
                    calls = self.extract_tool_calls(text)
                    if len(calls) > 0:
                        self.tool_calls = calls
                        return True
                except:
                    pass
        elif mode == 2:
            print("")

    # Getter Functions

    def get_default_system_prompt(self):
        prompt = open(os.path.abspath(os.path.join(
            __file__, "..", "resources", "chain_system_prompt.md")), "r", encoding="utf-8").read()
        if isinstance(self.toolkit, ChatToolKit):
            prompt += "\n\n" + self.toolkit.system_prompt()
        return prompt

    # Setter Functions

    def apply_default_system_prompt(self):
        self.messages.system(self.get_default_system_prompt())

    # Helper Functions

    @classmethod
    def extract_tool_calls(self, text: str) -> list:
        """
        Extracts all function calls from `tool`-prefixed blocks by matching nested parentheses correctly, 
        ignoring parentheses inside strings.

        :param call_text: The text containing multiple potential function calls.
        :returns: A list of complete function calls as strings, or an empty list if no valid calls are found.
        """
        # Find all `tool`-prefixed blocks enclosed in triple backticks
        # Non-greedy match for each block
        tool_blocks = re.findall(r'```tool\s+([\s\S]+?)```', text)

        function_calls = []  # Store all extracted function calls

        # Process each tool block to extract valid function calls
        for tool_content in tool_blocks:
            tool_content = tool_content.strip()

            # Find the start of a function call (word followed by an open parenthesis)
            start_match = re.search(r'\b(\w+)\s*\(', tool_content)
            if not start_match:
                continue  # No valid function call found, skip to the next block

            start_index = start_match.start()  # Start of the function call
            stack = []  # Track opening and closing parentheses
            in_string = None  # Track if we're inside a string (either ' or ")

            # Iterate through the content to find matching parentheses
            for i, char in enumerate(tool_content[start_index:], start=start_index):
                if char in ('"', "'"):  # Toggle in/out of string
                    if in_string is None:
                        in_string = char  # Entering a string
                    elif in_string == char:
                        in_string = None  # Exiting the string

                elif char == '(' and in_string is None:
                    stack.append('(')  # Track opening parenthesis

                elif char == ')' and in_string is None:
                    if stack:
                        stack.pop()  # Track closing parenthesis
                    if not stack:  # All parentheses matched
                        # Extract and store the function call
                        function_calls.append(tool_content[start_index:i + 1])
                        break  # Move to the next tool block

        return function_calls

    @classmethod
    def parse_function_calls(self, function_calls: list) -> list:
        """
        Parses a list of Python function call strings into structured data, extracting 
        function names, positional arguments, and keyword arguments.

        :param function_calls: List of valid Python function call strings.
        :returns: List of dictionaries, each containing 'name', 'args', and 'kwargs' keys.
        """
        parsed_calls = []

        for call in function_calls:
            try:
                # Parse the function call using the ast module
                tree = ast.parse(call.strip(), mode='eval')

                # Ensure the tree contains a valid Call node
                if isinstance(tree.body, ast.Call):
                    func_name = tree.body.func.id if isinstance(
                        tree.body.func, ast.Name) else None

                    # Extract positional arguments (args)
                    args = [ast.literal_eval(arg) for arg in tree.body.args]

                    # Extract keyword arguments (kwargs)
                    kwargs = {
                        kw.arg: ast.literal_eval(kw.value) for kw in tree.body.keywords
                    }

                    if func_name:  # Store only valid function names
                        parsed_calls.append(
                            {'name': func_name, 'args': args, 'kwargs': kwargs})

            except (SyntaxError, ValueError) as e:
                # Handle any parsing or literal evaluation errors gracefully
                print(f"Skipping invalid call: {call} - Error: {e}")

        return parsed_calls
