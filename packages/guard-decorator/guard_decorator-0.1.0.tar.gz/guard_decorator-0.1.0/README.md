# Guard

Guard is a Python library designed to simplify exception handling in your code. By using the `guard` decorator, you can significantly reduce the boilerplate code associated with `try-except-finally` blocks, making your code cleaner and more readable.

## Features

- **Simplified Exception Handling:** Easily handle exceptions with minimal boilerplate code.
- **custom Handlers:** Specify custom exception handlers for different exceptions.
- **Cleanup Actions:** Automatically perform cleanup actions after function execution, regardless of success or failure.
- **Support for Classes:** Use `guard` with class methods to maintain clean and effective error handling.

## Installation

You can install the `guard` library via pip:

```bash
pip install guard
```

## Basic usage:

```python
from guard import guard

# Exception handler
def handle_division_error(e, *args, **kwargs):
    print(f"Caught exception: {e}")

@guard(h=handle_division_error)
def divide_numbers(a, b):
    print(f"Dividing {a} by {b}")
    return a / b

print(f"Result: {divide_numbers(10, 2)}")   # OK
print(f"Result: {divide_numbers(10, 0)}")   # Raises Exception

```

That code will produce the following output:

```bash
Dividing 10 by 2
Result: 5.0
Dividing 10 by 0
Caught exception: division by zero
Result: None
```

## You can also specify exception type

```python
@guard(type=ValueError, h=handle_value_error)
def risky_function(value):
    if value < 0:
        raise ValueError("Negative value not allowed!")
```

## And cleanup actions

```python
def cleanup_file(*args, **kwargs):
    print("Cleaning up resources...")

@guard(f=cleanup_file)
def open_file(file_name):
    raise FileNotFoundError("File not found!") # Simulate error

open_file("non_existent_file.txt")

```

## License
This project is licensed under the Apache 2.0 License