# Object-Oriented Programming

Object-Oriented Programming (OOP) is a programming paradigm that organizes code around objects, which are instances of classes. It provides a way to structure and design programs by encapsulating related data and behavior into objects. OOP promotes the concepts of modularity, reusability, and extensibility. Python is an object-oriented programming language that fully supports OOP principles. Here's an overview of key concepts in OOP:

1. Class

- A class is a blueprint or template that defines the structure and behavior of objects.
- It encapsulates data (attributes) and functions (methods) that operate on that data.
- Objects are created from classes and are instances of those classes.

Example:

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2

# Creating objects (instances) of the Circle class
circle1 = Circle(5)
circle2 = Circle(3)

# Accessing attributes and calling methods
print(circle1.radius)  # Output: 5
print(circle2.calculate_area())  # Output: 28.26
```

1. Object

- An object is an instance of a class.
- It represents a specific entity or concept with its own unique state and behavior.
- Objects have their own set of attributes and can perform actions through methods.

1. Encapsulation

- Encapsulation is the bundling of data and related methods into a single unit (class).
- It hides the internal details of an object and provides an interface for interacting with the object.
- Encapsulation helps achieve data abstraction, data protection, and modularity.

1. Inheritance

- Inheritance allows a class (subclass) to inherit properties and methods from another class (superclass or parent class).
- It promotes code reuse and supports the concept of hierarchical relationships between classes.
- Subclasses can add new functionality or override inherited methods.

Example:

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Animal makes a sound.")


class Dog(Animal):
    def sound(self):
        print("Dog barks.")

dog = Dog("Buddy")
dog.sound()  # Output: Dog barks.
```

1. Polymorphism

- Polymorphism refers to the ability of objects to take on multiple forms.
- It allows objects of different classes to be treated as objects of a common superclass.
- Polymorphism enables code to be written that can work with objects of various types without explicit type checking.

Example:

```python
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    print(shape.area())

# Output:
# 78.5
# 24
```

1. Polymorphism

- Polymorphism refers to the ability of objects to take on multiple forms.
- It allows objects of different classes to be treated as objects of a common superclass.
- Polymorphism enables code to be written that can work with objects of various types without explicit type checking.

These are the core concepts of Object-Oriented Programming in Python. By utilizing these concepts, you can design and implement code that is modular, reusable, and easier