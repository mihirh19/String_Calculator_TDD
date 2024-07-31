# String Calculator TDD

This project implements a simple string calculator using Test-Driven Development (TDD) principles. The calculator can handle different delimiters, including commas and new lines, and can be configured to use custom delimiters. It also throws exceptions for negative numbers.

# Docker Image:
```
docker pull mihir2109/string_cal
```

# 🏭 Project Structure

    ├── src
    │   └── string_calculator.py
    ├── test
    │   ├──  test_string_calculator.py

# 🎯 Features

- Empty String: Returns 0.
- Single Number: Returns the number itself.
- Two Numbers: Returns the sum of two numbers.
- Multiple Numbers: Returns the sum of multiple numbers.
- New Lines: Supports new lines as delimiters.
- Custom Delimiters: Supports custom delimiters specified at the start of the input string.
- Negative Numbers: Throws an exception with a list of negative numbers.

# 🏗️ How It's Built

- Python 3.12
- pytest

# Installation

## 1. clone the repository

```
git clone https://github.com/mihirh19/String_Calculator_TDD.git
cd String_Calculator_TDD
```

## 2. Install Dependencies

```
pip install -r requirements.txt
```

## 3. Run the tests

```
pytest
```

# Testing with pytest

The pytest framework makes it easy to write small, readable tests, and can scale to support complex functional testing for applications and libraries.

# TestCases

`test_string_calculator.py`

- `test_add_empty_string()` : Test case for empty string returns 0.
- `test_add_single_number()`: Test case for single number returns the number.
- `test_add_two_numbers()` : Test case for two numbers returns the sum of the numbers.
- `test_add_three_numbers()` : Test case for three numbers returns the sum of the numbers.
- `test_add_many_numbers()` : Test case for many numbers returns the sum of the numbers.
- `test_add_newline_delimiter()` : Test case for new line delimiter returns the sum of the numbers.
- `test_add_custom_delimiter()` : Test case for custom delimiter returns the sum of the numbers.
- `test_add_custom_delimiter2()` : Test case for custom delimiter with length > 1 returns the sum of the numbers.
- `test_add_negative_numbers()` : Test case for negative numbers raises an error.
- `test_add_custom_delimiter_with_newline()` : Test case for custom delimiter as newline returns the sum of the numbers.
- `test_non_numeric_characters()` : Test case for non-numeric characters raises an error.
- `test_add_ignore_numbers_greater_than_1000()` : Test case for numbers greater than 1000 are ignored.
- `test_add_custom_delimiter_with_any_length()` : Test case for custom delimiter with any length returns the sum of the numbers.

## Author

👤 **Mihir Hadavani**

- Twitter: [@mihirh21](https://twitter.com/mihirh21)
- Github: [@mihirh19](https://github.com/mihirh19)
- LinkedIn: [@mihir-hadavani-996263232](https://linkedin.com/in/mihir-hadavani-996263232)
