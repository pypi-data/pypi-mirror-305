# Simple JSON Parser

A simple JSON parser implemented in Python without using any external libraries. This parser can handle a limited subset of JSON, including strings, numbers, objects, arrays, booleans, and null values.

## Features

- Parses JSON strings into Python data structures (dictionaries and lists).
- Supports basic JSON data types: strings, numbers, objects, arrays, booleans, and null.
- No external dependencies; written entirely in Python.

## Installation

You can simply copy the `JSONParser` class into your Python project. There is no need for installation via pip or any other package manager.

## Usage

To use the JSON parser, create an instance of the `JSONParser` class with a JSON string and call the `parse()` method. Here's an example:

```python
from json_parser import JSONParser  # Adjust the import based on your file structure

json_text = '{"name": "John", "age": 30, "is_student": false, "courses": ["Math", "Science"], "address": null}'
parser = JSONParser(json_text)
parsed_data = parser.parse()

print(parsed_data)
```

## Error Handling
The parser raises ValueError for various issues, such as:

Unexpected end of input
Invalid JSON values
Unterminated strings
Missing colons or commas in objects and arrays

## Limitations
This parser is a basic implementation and may not handle all edge cases or complex JSON structures.
It does not support JSON features like comments or special escape sequences in strings.