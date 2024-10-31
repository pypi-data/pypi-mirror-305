# chainollama

[![PyPI version](https://badge.fury.io/py/chainollama.svg)](https://badge.fury.io/py/chainollama)

**chainollama** is a partner package for chatollama which provides the `ChainEngine` class. This engine is an extension of the `ChatEngine` class. It provides a function called `chain(message: str)`. This function acts similarly to the `chat` function from `ChatEngine`, but it allows the model to respond both naturally and with tool calls sequentially. When the model is responding to the user's message, it is instructed to respond in a specific format if it wants to call tools that you can provide with the `ChatToolKit` and `ChatTool` classes.

Any Python function you create can be added to this system without the need for manual formatting. You just need to make the function, and the model will understand it. Ensure that you provide a description in the function like this:

```python
def testing_func(arg1: str, arg2: bool = True) -> None:
    """
    This is a test function with 2 arguments
    :param arg1: description for arg1
    :param arg2: description for arg2
    :returns: description of returning value(s)
    """
    return None
```

This function will be turned into this for the model to understand:

```json
{
    "function": "testing_func(arg1: str, arg2: bool = True) -> None",
    "description": "This is a test function with 2 arguments\n:param arg1: description for arg1\n:param arg2: description for arg2\n:returns: description of returning value(s)"
}
```

Note that while the `ChatTool` class exists to create individual tools, it is often easier to simply pass your functions directly into the `ChatToolKit` as a list. The toolkit will automatically convert these functions into tools without requiring you to create each `ChatTool` manually.

## Important Details About the Chain Function

The `chain` function internally uses the `chat` and `wait` functions. The `chat` function streams the response and runs as part of a separate thread, while the `wait` function allows you to wait for that thread to finish in the normal `chatollama` module. In `ChainEngine`, these functions are used internally, meaning that if you want to have the entire chain process run asynchronously, you will need to manage it by starting a separate thread yourself.

This approach means that no code will run after the `chain` function is called until the model completes its entire response cycle, including tool usage. This can be beneficial as it simplifies interaction, ensuring that everything is complete before moving forward. However, for scenarios involving UI performance or where responsiveness is key, handling threading on top of it is essential to maintain smooth operation.

## Fine-Tuning Plans

We are planning to create a fine-tuned version of the `llama3.1:8b` model that will be optimized to work even better with this system. This fine-tuned model will have several enhanced capabilities:

- **Improved Tool Use Integration**: The model will be better at weaving tool use naturally into its language responses.
- **Enhanced JSON Understanding**: The model will have a better understanding of the JSON format used for converting functions in the toolkit.
- **Internal System Command Awareness**: It will be trained to properly consider internal user system commands that allow the model to receive function results and continue responding seamlessly.
- **Overall System Integration**: The fine-tuned model will have a much better overall integration with the system, leading to more reliable interactions.

Currently, the normal `llama3.1:8b` model works fairly well, achieving around 50% success in properly using tools and responding to all components of the user's prompt. However, it sometimes forgets to use available tools or fails to respond to certain parts of a user's message. With fine-tuning, we expect this accuracy to improve significantly, aiming for 90% or better.

## Features

- **Chain Execution**: Allows the AI to perform tasks by sequentially combining natural language responses with tool calls.
- **Automatic Function Integration**: Any Python function can be added to the toolkit without manual formatting. The model automatically interprets the function signature and description.
- **Tool Calling Format**: Uses a consistent format for the AI to call tools, maintaining a seamless user experience while leveraging available functions.
- **Error Handling**: Includes robust error-handling mechanisms to ensure graceful recovery in case of tool call errors or unexpected input formats.
- **Extensible ToolKit**: Provides `ChatTool` and `ChatToolKit` classes to easily create and manage available tools for the model.

## Response Handling Callbacks

The `ChainEngine` provides two callbacks that developers can use to handle how the AI response is integrated into their application:

- **Before Chain Handle Callback (********`before_chain_handle_callback`********\*\*\*\*)**: This callback is called before the AI handles the response. It allows developers to manipulate or intercept the AI's output before processing. If this callback returns `True`, it will stop the streaming response immediately.

- **After Chain Handle Callback (********`after_chain_handle_callback`********\*\*\*\*)**: This callback is called after the AI processes the response. It allows developers to perform actions based on the processed output, such as modifying the final response or integrating it with the application. Similar to the `before` callback, if it returns `True`, it will stop further processing.

Both callbacks take the following arguments:

- **`mode`**\*\* (int)\*\*: Indicates the mode of the response (mode 0: starting a new response just before the model begins streaming, mode 1: runs for every token generated during streaming, mode 2: called one last time after the stream finishes).
- `delta`\*\* (str)\*\*: Represents the incremental part of the response being streamed. The current token generated basically.
- **`text`**\*\* (str)\*\*: The entire response text generated so far.

There is also a **default printing** mechanism (`default_printing`) which is enabled by default. This feature will print the AI's response in real-time as it is being streamed, allowing developers to see the process directly in the console. However, if either of the callbacks returns `True`, it will stop the stream immediately, providing greater control over how the output is handled.

## Examples

Below are some simple usage examples to demonstrate how to use `chainollama` effectively.

### Example 1: Adding a Function to ChatToolKit

```python
from chainollama import ChatToolKit, ChainEngine

# Define a sample function
def greet_user(name: str) -> str:
    """
    Greets the user by name.
    :param name: The name of the user to greet
    :returns: A greeting string
    """
    return f"Hello, {name}!"

# Add the function to the ChatToolKit
toolkit = ChatToolKit([greet_user])
```

### Example 2: Using ChainEngine to Respond with a Tool Call

```python
# Initialize the ChainEngine with the toolkit
engine = ChainEngine(model="llama3.1:8b", toolkit=toolkit)

# Use the chain method to interact
engine.chain("Greet the user named John.")

# Output could be something like:
# "Hello, John!"
```

### Example 3: Handling Multiple Tools

```python
# Define more functions
def add_numbers(a: int, b: int) -> int:
    """
    Adds two numbers.
    :param a: The first number
    :param b: The second number
    :returns: The sum of the two numbers
    """
    return a + b

def multiply_numbers(a: int, b: int) -> int:
    """
    Multiplies two numbers.
    :param a: The first number
    :param b: The second number
    :returns: The product of the two numbers
    """
    return a * b

# Add the functions to the toolkit
toolkit = ChatToolKit([add_numbers, multiply_numbers])

# Initialize the ChainEngine again
engine = ChainEngine(model="llama3.1:8b", toolkit=toolkit)

# Use the chain method to interact
engine.chain("What is 5 plus 3?")
# Output: "The result of 5 plus 3 is 8."

engine.chain("What is 4 times 7?")
# Output: "The result of 4 times 7 is 28."
```

