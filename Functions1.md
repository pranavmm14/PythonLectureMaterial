# Python Functions

## Built-in Functions
Python provides many built-in functions like `print()`, `len()`, `type()`, etc.

Example:
```python
print("Hello, World!")
length = len("Hello")
print(length)
```

## User Defined Function
You can create your own functions using the `def` keyword.

Example:
```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
```

## Docstrings
Docstrings are used to document a function, class, or module. They are defined using triple quotes.

Example:
```python
def add(a, b):
    """
    This function adds two numbers.
    
    Parameters:
    a (int): The first number.
    b (int): The second number.
    
    Returns:
    int: The sum of the two numbers.
    """
    return a + b

print(add(2, 3))
print(add.__doc__)
```

## Calling a Function in Python
Functions are called by using their name followed by parentheses.

Example:
```python
def say_hello():
    return "Hello!"

print(say_hello())
```

## Types of Arguments
1. **Positional Arguments**
2. **Keyword Arguments**
3. **Default Arguments**

Example:
```python
def describe_person(name, age=30):
    print(f"Name: {name}, Age: {age}")

describe_person("Alice", 25)   # Positional Arguments
describe_person(age=28, name="Bob")  # Keyword Arguments
describe_person("Charlie")  # Default Argument for age
```

## Variable Length Arguments

In Python, you can define functions that can accept a variable number of arguments. This is useful when you don't know beforehand how many arguments might be passed to your function. There are two types of variable length arguments:

1. **Arbitrary Positional Arguments (`*args`)**
2. **Arbitrary Keyword Arguments (`**kwargs`)**

### 1. Arbitrary Positional Arguments (`*args`)

When you prefix a parameter with an asterisk (`*`), it collects all the additional positional arguments passed to the function into a tuple. This allows you to pass a varying number of positional arguments to your function.

#### Example:
```python
def sum_all(*args):
    """
    This function sums all the positional arguments passed to it.
    
    Parameters:
    *args (tuple): Variable length argument list of numbers to be summed.
    
    Returns:
    int/float: The sum of all the arguments.
    """
    return sum(args)

print(sum_all(1, 2, 3, 4))  # Output: 10
print(sum_all(5, 10, 15))   # Output: 30
```

### 2. Arbitrary Keyword Arguments (`**kwargs`)

When you prefix a parameter with two asterisks (`**`), it collects all the additional keyword arguments passed to the function into a dictionary. This allows you to pass a varying number of keyword arguments to your function.

#### Example:
```python
def print_info(**kwargs):
    """
    This function prints out key-value pairs of all the keyword arguments passed to it.
    
    Parameters:
    **kwargs (dict): Variable length argument dictionary of key-value pairs.
    """
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="New York")
# Output:
# name: Alice
# age: 25
# city: New York
```

### Combining `*args` and `**kwargs`

You can use both `*args` and `**kwargs` in the same function definition to accept both positional and keyword arguments.

#### Example:
```python
def mix_args(*args, **kwargs):
    """
    This function prints out positional and keyword arguments passed to it.
    
    Parameters:
    *args (tuple): Variable length argument list of positional arguments.
    **kwargs (dict): Variable length argument dictionary of keyword arguments.
    """
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

mix_args(1, 2, 3, name="Alice", age=25)
# Output:
# Positional arguments: (1, 2, 3)
# Keyword arguments: {'name': 'Alice', 'age': 25}
```

### Use Cases

1. **Flexible Function Interfaces**: Functions that accept variable length arguments are flexible and can handle different numbers of inputs.
2. **Wrapper Functions**: They are useful in writing wrapper functions that need to accept arbitrary arguments and pass them to other functions.

#### Wrapper Function Example:
```python
def log_args(func):
    """
    A decorator that logs the arguments passed to the function.
    
    Parameters:
    func (function): The function to be decorated.
    
    Returns:
    function: The decorated function.
    """
    def wrapper(*args, **kwargs):
        print("Arguments:", args)
        print("Keyword Arguments:", kwargs)
        return func(*args, **kwargs)
    
    return wrapper

@log_args
def multiply(a, b):
    return a * b

print(multiply(2, 3))
# Output:
# Arguments: (2, 3)
# Keyword Arguments: {}
# 6
```

## Scope of Variables
Variables have different scopes, mainly Local, Enclosing, Global, and Built-in scopes.

Example:
```python
global_var = "Global"

def outer_function():
    enclosing_var = "Enclosing"
    
    def inner_function():
        local_var = "Local"
        print(local_var)
        print(enclosing_var)
        print(global_var)
        
    inner_function()

outer_function()
```

## Types of Variables
1. **Local Variables**: Defined inside a function.
2. **Global Variables**: Defined outside of any function.
3. **Nonlocal Variables**: Defined in the enclosing function.

Example:
```python
def outer():
    nonlocal_var = "Nonlocal"

    def inner():
        local_var = "Local"
        print(local_var)
        print(nonlocal_var)
        
    inner()

outer()

global_var = "Global"
print(global_var)
```

## Recursive Functions
A recursive function is a function that calls itself.

Example:
```python
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))
```

## Namespaces
A namespace is a container where names are mapped to objects. Python uses different namespaces like local, global, and built-in.

Example:
```python
var = "Global Variable"

def foo():
    var = "Local Variable"
    print(var)

foo()
print(var)
```

## Nested Functions
A function defined inside another function is called a nested function.

Example:
```python
def outer_function():
    def inner_function():
        return "Hello from inner function"
    
    return inner_function()

print(outer_function())
```

## Benefits of Functions
1. **Code Reusability**: Functions allow code to be reused without rewriting it.
2. **Modularity**: Functions break the code into smaller parts, making it easier to manage.
3. **Readability**: Well-named functions make the code easier to understand.
4. **Testing**: Functions can be tested independently.

Example:
```python
def calculate_area(radius):
    return 3.14 * radius * radius

print(calculate_area(5))
```
---
&copy; Pranav Mehendale, Yashashri Computers, Kothrud, Pune 2024. All rights reserved. This material is for non-commercial use only.

---