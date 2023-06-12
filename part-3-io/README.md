# Input and Output

In Python, input and output (I/O) operations refer to the process of receiving data from the user (input) and displaying or writing data to the screen, files, or other devices (output). Here's an overview of input and output operations in Python:

## Input

- The `input()` function is used to receive input from the user.
- It prompts the user with a message or question and waits for the user to enter data.
- The input is read as a string by default.
- You can assign the input to a variable to store and use the entered value in your program.

Example:

```python
name = input("Enter your name: ")
print("Hello, " + name + "!")
```

In the example above, the `input()` function prompts the user to enter their name. The entered value is assigned to the variable `name`, which is then used to print a greeting message.

## Output

- The `print()` function is used to display output to the screen.
- It takes one or more arguments, which can be strings, variables, or expressions.
- The `print()` function outputs the values separated by spaces by default and adds a newline character at the end.
- You can customize the separator and the end character using the `sep` and `end` parameters of the `print()` function.

Example:

```python
name = "John"
age = 25
print("Name:", name, "Age:", age)
```

In the example above, the `print()` function displays the values of `name` and `age`, separated by spaces. The output will be "Name: John Age: 25" followed by a newline.

File I/O:

- Python provides functions and methods for working with files to perform input and output operations on external files.
- The `open()` function is used to open a file and returns a file object.
- File objects have methods such as `read()`, `readline()`, and `write()` to read or write data to and from files.
- After working with a file, it's important to close it using the `close()` method of the file object or by using a context manager (`with` statement).

Example (Writing to a file):

```python
with open("output.txt", "w") as file:
    file.write("Hello, World!")
```

In the example above, the `open()` function is used to open the file named "output.txt" in write mode. The `write()` method of the file object is then used to write the text "Hello, World!" to the file.

Example (Reading from a file):

```python
with open("input.txt", "r") as file:
    data = file.read()
    print(data)
```

In the example above, the `open()` function is used to open the file named "input.txt" in read mode. The `read()` method of the file object is used to read the entire contents of the file, which is then printed using the `print()` function.

Input and output operations are essential for interacting with users, displaying results, and working with external data in Python. Understanding and utilizing these operations effectively allows you to build interactive programs and work with various data sources.
