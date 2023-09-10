# functions.py

def greet_programmer():
    """Greets the programmer with a default message."""
    print("Hello, programmer!")

def greet(name):
    """Greets a person with a custom message."""
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    """Greets a person with a custom message or a default message."""
    print(f"Hello, {name}!")

def add(a, b):
    """Adds two numbers and returns the result."""
    return a + b

def halve(number):
    """Divides a number by 2 and returns the result."""
    return number / 2
