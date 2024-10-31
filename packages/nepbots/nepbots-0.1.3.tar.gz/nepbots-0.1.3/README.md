
# Nepbots

A simple API wrapper for Nepbots that allows you to query and get answers from the Nepbots API.

## Installation

```bash
pip install nepbots
```

## Usage

Here's a quick example of how to use the `nepbots` package:

### Import the Module

First, import the `NepbotsApi` class from the package:

```python
from nepbots import NepbotsApi
```

### Create an Instance

Create an instance of the `NepbotsApi` class:

```python
api = NepbotsApi()
```

### Get an Answer

You can now use the `get_answer` method to ask a question. For example:

```python
question = "What is the capital of France?"  # You can change this question to anything you like.
answer = api.get_answer(question)
print(answer)  # Output will be: Hello! How can I assist you today? (creator: glitchyapi)
```

### Full Example

Here’s a complete example script that puts it all together:

```python
# example_script.py
from nepbots import NepbotsApi

def main():
    api = NepbotsApi()
    question = "What is the capital of France?"  # Change this to test different questions
    answer = api.get_answer(question)
    print(answer)  # Print only the answer with creator info

if __name__ == "__main__":
    main()

```

### Note

- Ensure you have an active internet connection since the package interacts with an external API.
- The answer may vary depending on the API's response.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

Created by (creator: t.me/nepcoderapis).
```

