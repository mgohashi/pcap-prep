# Fundamentals

## Comments

Comments in programming are lines of text that are ignored by the interpreter or compiler and serve as notes or explanations within the code. They are used to provide additional information about the code, improve its readability, and make it easier for developers to understand and maintain. In Python, comments are denoted using the `#` symbol. Here are some key points about comments:

1. Single-Line Comments:
A single-line comment starts with the `#` symbol and extends until the end of the line. It is used to provide short explanations or annotations about a specific line of code.

Example:

```python
# This is a single-line comment
x = 5  # Assigning a value to variable x
```

1. Multi-Line Comments:
In Python, there is no built-in syntax for multi-line comments like `/* ... */` in some other programming languages. However, you can use multiple single-line comments consecutively to achieve a similar effect.

Example:

```python
# This is a multi-line comment
# It spans across multiple lines
x = 5
```

1. Commenting Best Practices:

- Use comments to explain complex or non-obvious sections of code to improve its understandability.
- Avoid redundant or excessive comments that simply restate the obvious.
- Comment code that is difficult to understand, has potential risks, or requires further explanation.
- Follow consistent commenting styles and conventions within a project or team to maintain code readability.
- Update comments when modifying code to keep them accurate and relevant.

1. Documentation Strings (Docstrings):
Apart from comments, Python has a special type of comment called docstrings. Docstrings are used to document modules, functions, classes, and methods. They provide more extensive documentation and can be accessed programmatically.

Example:

```python
def calculate_area(length, width):
    """Calculate the area of a rectangle.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The area of the rectangle.
    """
    return length * width
```

Docstrings are enclosed in triple quotes (`""" ... """`) and follow a specific format. They typically include information about the function's purpose, arguments, return values, and any exceptions that may be raised.

1. Commenting for Debugging:
Comments can also be used for temporary debugging purposes. By commenting out sections of code, you can temporarily disable their execution without deleting them. This allows you to test alternative code or isolate problematic areas.

Example:

```python
# print("This code is executed")
# print("This code is not executed")
```

Comments play an important role in maintaining well-documented and understandable code. They help communicate the intent, logic, and important details of the code to other developers, including your future self. Writing clear and concise comments can greatly assist in code maintenance, collaboration, and debugging efforts.

## Variables

In Python, variables are used to store and manipulate data. They act as containers that hold values of different data types. Here are the main data types in Python:

1. Numeric Types:
   - Integer (``int``): Represents whole numbers, such as 5, -2, or 0.
   - Floating-Point Number (``float``): Represents decimal numbers, such as 3.14, -0.5, or 2.0.

1. String (``str``):
   - Represents a sequence of characters enclosed in single quotes ('') or double quotes ("").

     Example: ``"Hello, World!"``

1. Boolean (``bool``):
   - Represents either true or false.
   - Used in logical operations and control flow.

     Example: ``True``, ``False``

1. List (``list``):
   - Represents an ordered collection of items.
   - Items can be of different data types.
   - Enclosed in square brackets [] and separated by commas.

     Example: ``[1, 2, 3, "apple", True]``

1. Tuple (``tuple``):
   - Similar to lists but immutable (cannot be modified once created).
   - Enclosed in parentheses () and separated by commas.

     Example: ``(1, 2, 3, "apple", True)``

1. Dictionary (``dict``):
   - Represents a collection of key-value pairs.
   - Keys are unique and used to access corresponding values.
   - Enclosed in curly braces {} and separated by commas.

     Example: ``{"name": "John", "age": 25, "city": "New York"}`` or ``dict(name="John", age=25, city="New York")``

1. Set (``set``):
   - Represents an unordered collection of unique elements.
   - Enclosed in curly braces {} or created using the set() function.

     Example: ``{1, 2, 3, 4, 5}`` or ``set([1, 2, 3, 4, 5])``

1. ``None`` (NoneType):
   - Represents the absence of a value or a null value.
   - Often used to initialize variables or indicate the absence of a return value.

Python is a dynamically typed language, which means you don't need to explicitly declare the data type of a variable. The interpreter determines the data type based on the assigned value. For example:

```python
x = 5          # x is an integer
y = 3.14       # y is a float
name = "John"  # name is a string
```

You can also use type conversion functions to convert variables from one data type to another. For example, ``int()``, ``float()``, ``str()``, etc.

Understanding and utilizing the appropriate data types is essential for performing operations and manipulating data effectively in Python.

## Operators

In Python, operators are symbols or special keywords that perform operations on operands (values or variables). They allow you to manipulate and combine data in various ways. Here are the main types of operators in Python:

1. Arithmetic Operators:
   - Addition (``+``): Adds two operands.
   - Subtraction (``-``): Subtracts the second operand from the first.
   - Multiplication (``*``): Multiplies two operands.
   - Division (``/``): Divides the first operand by the second (returns a float).
   - Floor Division (``//``): Divides the first operand by the second and rounds down to the nearest integer.
   - Modulus (``%``): Returns the remainder of the division.
   - Exponentiation (``**``): Raises the first operand to the power of the second.

1. Comparison Operators:
   - Equal to (``==``): Checks if two operands are equal.
   - Not equal to (``!=``): Checks if two operands are not equal.
   - Greater than (``>``): Checks if the left operand is greater than the right.
   - Less than (``<``): Checks if the left operand is less than the right.
   - Greater than or equal to (``>=``): Checks if the left operand is greater than or equal to the right.
   - Less than or equal to (``<=``): Checks if the left operand is less than or equal to the right.

1. Logical Operators:
   - Logical AND (``and``): Returns True if both operands are true.
   - Logical OR (``or``): Returns True if at least one operand is true.
   - Logical NOT (``not``): Returns the opposite of the operand's truth value.

1. Assignment Operators:
   - Assignment (``=``): Assigns the value on the right to the variable on the left.
   - Compound assignment operators (e.g., ``+=``, ``-=``, ``*=``): Perform an operation and assign the result to the variable.

1. Membership Operators:
   - ``in``: Checks if a value exists in a sequence (e.g., list, string, tuple).
   - ``not in``: Checks if a value does not exist in a sequence.

1. Identity Operators:
   - ``is``: Checks if two operands refer to the same object.
   - ``is not``: Checks if two operands do not refer to the same object.

1. Bitwise Operators (operate on binary representations of integers):
   - Bitwise AND (``&``): Performs a bitwise AND operation.
   - Bitwise OR (``|``): Performs a bitwise OR operation.
   - Bitwise XOR (``^``): Performs a bitwise exclusive OR operation.
   - Bitwise NOT (``~``): Flips the bits of the operand.
   - Left Shift (``<<``): Shifts the bits of the left operand to the left by a specified number of positions.
   - Right Shift (``>>``): Shifts the bits of the left operand to the right by a specified number of positions.

These operators allow you to perform calculations, compare values, combine conditions, manipulate bits, and assign values in Python. Understanding and using operators correctly is crucial for writing effective and efficient code.

## Control flow

Control flow refers to the order in which statements and instructions are executed in a program. In Python, control flow is managed using various control structures that allow you to make decisions, repeat blocks of code, and alter the program's execution flow. The main control flow structures in Python are:

1. Conditional Statements (``if-elif-else``):

   - The if statement allows you to execute a block of code if a specified condition is true.
   - The elif statement (short for "else if") provides additional condition checks.
   - The else statement specifies a block of code to execute if none of the previous conditions are true.
   - Example:

     ```python
     if condition1:
         # code to execute if condition1 is true
     elif condition2:
         # code to execute if condition2 is true
     else:
         # code to execute if none of the above conditions are true
     ```

1. Loops:
   - The while loop executes a block of code repeatedly as long as a condition is true.
   - The for loop iterates over a sequence (such as a list or string) or other iterable objects.
   - Example:

     ```python
     while condition:
        # code to execute as long as the condition is true
     for item in sequence:
        # code to execute for each item in the sequence
     ```

1. Loop Control Statements:
   - The ``break`` statement terminates the loop prematurely, skipping the remaining iterations.
   - The ``continue`` statement skips the current iteration and moves to the next iteration.
   - The ``pass`` statement is a placeholder that does nothing. It is often used when a statement is required syntactically, but no action is needed.
   - Example:

     ```python
        for item in sequence:
           if condition:
              break  # terminate the loop
  
           if another_condition:
              continue  # skip current iteration and move to the next
  
           # code to execute for each item
  
        while condition:
           pass  # placeholder statement
      ```

1. Exception Handling (``try-except``):
   - The try block is used to enclose code that might raise exceptions.
   - The except block specifies the actions to take if a specific exception occurs.
   - Example:

     ```python
     try:
         # code that may raise exceptions
     except ExceptionType1:
         # code to handle ExceptionType1
     except ExceptionType2:
         # code to handle ExceptionType2
     else:
         # code to execute if no exceptions occurred
     finally:
         # code that always executes, regardless of exceptions
     ```

These control flow structures allow you to create programs with branching paths, repetitive operations, and exception handling. They give you control over how your code is executed and allow you to handle different scenarios effectively.

## Functions

In Python, a function is a reusable block of code that performs a specific task. Functions provide modularity and allow you to break down complex tasks into smaller, more manageable pieces. They help organize code, promote code reusability, and improve readability. Here are the key aspects of functions in Python:

Function Definition:

- A function is defined using the ``def`` keyword followed by the function name and parentheses ``( )``.
- Parameters (optional) are specified within the parentheses, separated by commas, to receive input values.
- The function definition ends with a colon ``:``.

Function Body:

- The function body consists of the code block that is executed when the function is called.
- It is indented under the function definition.
- The body can contain any valid Python code, including variable assignments, control flow statements, and other function calls.

Function Invocation (Calling):

- To execute a function, you call it by using its name followed by parentheses ``( )``.
- If the function has parameters, you provide the corresponding arguments within the parentheses.
- The function call can be assigned to a variable or used as an argument in other expressions.

Function Return:

- Functions can optionally return a value using the ``return`` statement.
- The ``return`` statement terminates the function execution and sends the value back to the caller.
- If no ``return`` statement is used, the function returns None by default.

Function Example:

```python
 def greet(name):
     """This function greets the person with the given name."""
     print("Hello, " + name + "!")
 # Function call
 greet("John")  # Output: Hello, John!
```

In the example above:

- The function ``greet`` is defined with a single parameter ``name``.
- When the function is called with the argument ``"John"``, it prints the greeting ``"Hello, John!"``.

Function Documentation:

- Functions can have documentation strings (docstrings) enclosed in triple quotes ``""" """``.
- Docstrings provide information about the function's purpose, parameters, and return values.
- They can be accessed using the ``help()`` function or by accessing the ``__doc__`` attribute of the function object.

Function Parameters:

- Parameters are variables defined within the function's parentheses that receive values from the caller.
- Functions can have zero or more parameters.
- Parameters can have default values, making them optional during function invocation.

Function Arguments:

- Arguments are the actual values passed to a function during its invocation.
- They can be literals, variables, or expressions.
- Arguments are mapped to parameters based on their order or by using keyword arguments.

Function Overloading:

- Python does not support function overloading in the traditional sense (multiple functions with the same name but different parameter types or counts).
- However, you can use default parameter values or variable-length argument lists to achieve similar functionality.

Functions are a fundamental concept in Python programming. They allow you to organize code, modularize tasks, and promote code reuse. By defining and using functions effectively, you can write cleaner, more maintainable, and more efficient code.

## String

String manipulation in Python refers to the process of manipulating and modifying strings, which are sequences of characters. Python provides a variety of built-in string methods and operations that allow you to perform various tasks, such as concatenation, slicing, searching, replacing, and formatting. Here's an overview of string manipulation in Python:

1. Concatenation:

- You can concatenate strings using the `+` operator or the `+=` assignment operator.
- Concatenation merges two or more strings into a single string.

Example:

```python
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)  # Output: John Doe
```

1. Slicing:

- Slicing allows you to extract a portion of a string based on indices.
- You can use square brackets `[]` to specify the start and end indices, and an optional step value.
- Slicing returns a new string containing the extracted portion.

Example:

```python
message = "Hello, World!"
print(message[7:12])  # Output: World
```

1. String Methods:

- Python provides numerous built-in string methods for common string operations.
- Some commonly used methods include `lower()`, `upper()`, `strip()`, `split()`, `replace()`, `find()`, and `count()`.
- These methods return modified versions of the original string or perform specific tasks on the string.

Example:

```python
message = "   Hello, World!   "
print(message.strip())  # Output: Hello, World!
print(message.replace("Hello", "Hi"))  # Output:    Hi, World!   
```

1. String Formatting:

- String formatting allows you to create dynamic strings by combining variables or values with specific formats.
- Python supports multiple approaches for string formatting, including using the `%` operator, the `format()` method, and f-strings (formatted string literals).

Example:

```python
name = "John"
age = 25
print("My name is %s and I am %d years old." % (name, age))
print("My name is {} and I am {} years old.".format(name, age))
print(f"My name is {name} and I am {age} years old.")
```

1. String Manipulation with Regular Expressions:

- Regular expressions (regex) provide a powerful way to manipulate and search for patterns in strings.
- The `re` module in Python allows you to work with regular expressions.
- With regex, you can perform tasks like pattern matching, searching, substitution, and validation.

Example:

```python
import re

text = "The quick brown fox jumps over the lazy dog."
pattern = r"\b\w{4}\b"  # Matches four-letter words
matches = re.findall(pattern, text)
print(matches)  # Output: ['over', 'lazy', 'dog']
```

String manipulation is a crucial aspect of working with textual data in Python. By using string methods, slicing, and regular expressions, you can perform a wide range of operations on strings, such as manipulating their contents, searching for specific patterns, extracting information, and formatting output. Understanding and utilizing these string manipulation techniques can greatly enhance your ability to process and transform text data in Python.

## Math

The `math` module in Python provides a wide range of mathematical functions and constants. It is part of the Python Standard Library and offers various features for performing mathematical operations. Here are some of the main features of the `math` module:

1. Mathematical Constants:
The `math` module includes constants such as pi (π) and Euler's number (e), which are commonly used in mathematical calculations.

Example:

```python
import math

print(math.pi)  # Output: 3.141592653589793
print(math.e)   # Output: 2.718281828459045
```

1. Trigonometric Functions:
The `math` module provides trigonometric functions for angles in radians, including sine, cosine, tangent, and their inverses.

Example:

```python
import math

angle = math.pi / 4  # 45 degrees in radians

print(math.sin(angle))    # Output: 0.7071067811865476 (sine)
print(math.cos(angle))    # Output: 0.7071067811865476 (cosine)
print(math.tan(angle))    # Output: 1.0 (tangent)
print(math.asin(0.5))     # Output: 0.5235987755982989 (inverse sine)
print(math.acos(0.5))     # Output: 1.0471975511965979 (inverse cosine)
print(math.atan(1))       # Output: 0.7853981633974483 (inverse tangent)
```

1. Exponential and Logarithmic Functions:
The `math` module provides functions for exponential and logarithmic operations, such as raising a number to a power, calculating logarithms, and exponential functions.

Example:

```python
import math

print(math.exp(2))        # Output: 7.3890560989306495 (e raised to the power of 2)
print(math.log(10))       # Output: 2.302585092994046 (natural logarithm of 10)
print(math.log10(100))    # Output: 2.0 (base 10 logarithm of 100)
print(math.sqrt(25))      # Output: 5.0 (square root of 25)
```

1. Mathematical Functions:
The `math` module includes various mathematical functions, such as rounding, absolute value, factorial, and more.

Example:

```python
import math

print(math.ceil(4.3))       # Output: 5 (round up to the nearest integer)
print(math.floor(4.7))      # Output: 4 (round down to the nearest integer)
print(math.fabs(-4.5))      # Output: 4.5 (absolute value)
print(math.factorial(5))    # Output: 120 (factorial of 5)
print(math.abs(-5))        # Output: 5
print(math.abs(3.14))      # Output: 3.14
print(math.abs(-10.5))     # Output: 10.5
print(math.abs(-2 + 3j))   # Output: 3.605551275463989
```

1. Other Functions:
The `math` module provides additional functions for mathematical operations, including power, remainder, degrees to radians conversion, and radians to degrees conversion.

Example:

```python
import math

print(math.pow(2, 3))        # Output: 8.0 (2 raised to the power of 3)
print(math.remainder(10, 3))  # Output: 1.0 (remainder of 10 divided by 3)
print(math.degrees(math.pi))  # Output: 180.0 (convert radians to degrees)
print(math.radians(180))      # Output: 3.141592653589793 (convert degrees to radians)
```

These are some of the main features of the `math` module in Python. It provides a wide range of mathematical functions and constants that can

## Random

The `random` module in Python provides functions for generating random numbers and performing random operations. It is part of the Python Standard Library and offers various features for randomization. Here are some key aspects of the `random` module:

1. Generating Random Numbers:
The `random` module allows you to generate random numbers using different functions, including:

- `random()`: Returns a random floating-point number between 0 and 1 (inclusive of 0 but exclusive of 1).
  
  Example:

  ```python
  import random
  
  print(random.random())  # Output: 0.7168496849854194
  ```

- `randrange(start, stop, step)`: Returns a randomly selected element from the specified range.
  
  Example:

  ```python
  import random
  
  print(random.randrange(1, 10))       # Output: Random number between 1 and 9
  print(random.randrange(0, 101, 5))   # Output: Random multiple of 5 between 0 and 100
  ```

- `randint(a, b)`: Returns a random integer between the two specified values, inclusive of both endpoints.
  
  Example:

  ```python
  import random
  
  print(random.randint(1, 6))  # Output: Random number between 1 and 6
  ```

1. Shuffling and Sampling:
The `random` module provides functions for shuffling sequences randomly and sampling elements randomly.

- `shuffle(sequence)`: Randomly shuffles the elements of the given sequence in place.
  
  Example:

  ```python
  import random
  
  numbers = [1, 2, 3, 4, 5]
  random.shuffle(numbers)
  print(numbers)  # Output: Randomly shuffled list of numbers
  ```

- `sample(population, k)`: Returns a random sample of k unique elements from the given population without replacement.
  
  Example:

  ```python
  import random
  
  numbers = [1, 2, 3, 4, 5]
  sample = random.sample(numbers, 3)
  print(sample)  # Output: Random sample of 3 unique numbers from the list
  ```

1. Random Choices:
The `random` module provides functions for making random choices from a sequence or weighted choices.

- `choice(sequence)`: Returns a random element from the given sequence.
  
  Example:

  ```python
  import random
  
  fruits = ['apple', 'banana', 'cherry', 'durian']
  print(random.choice(fruits))  # Output: Randomly chosen fruit from the list
  ```

- `choices(population, weights=None, k=1)`: Returns a list of k elements randomly chosen from the population. The weights parameter allows you to specify the probability weights for each element.
  
  Example:

  ```python
  import random
  
  fruits = ['apple', 'banana', 'cherry', 'durian']
  weights = [0.4, 0.3, 0.2, 0.1]
  sample = random.choices(fruits, weights=weights, k=2)
  print(sample)  # Output: Randomly chosen fruits based on weights
  ```

1. Random Seed:
The `random` module allows you to set a random seed value using the `seed()` function. Setting the seed to a specific value ensures that the sequence of random numbers generated remains the same across different runs of the program, making the results reproducible.

Example:

```python
import random

random.seed(123)
print(random.random())  # Output: 0.052363598850944326

random
```
