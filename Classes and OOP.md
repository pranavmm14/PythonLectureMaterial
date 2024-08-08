# Python Classes and Object-Oriented Programming Concepts

## Introduction to Classes in Python

In Python, a class is a blueprint for creating objects, encapsulating data and methods that operate on that data. Objects are instances of classes.

### Defining a Class

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        return f"{self.name} says woof!"
```

- `__init__` initializes object attributes.
- `self` refers to the instance.

### Creating an Object

```python
my_dog = Dog("Buddy", 3)
print(my_dog.bark())  # Output: Buddy says woof!
```

## Inheritance

Inheritance allows a class to inherit attributes and methods from another class, promoting code reuse and establishing relationships.

### Single Inheritance

A class inherits from one base class.

```python
class Animal:
    def eat(self):
        return "Eating"

class Dog(Animal):
    def bark(self):
        return "Woof!"
```

### Multiple Inheritance

A class inherits from multiple base classes.

```python
class Flyable:
    def fly(self):
        return "Flying"

class Swimmable:
    def swim(self):
        return "Swimming"

class Duck(Flyable, Swimmable):
    def quack(self):
        return "Quack"
```

### Method Resolution Order (MRO)

MRO determines the order in which base classes are searched when executing a method. Use `.__mro__` or `mro()` method to view MRO.

```python
print(Duck.__mro__)
```

### Multilevel Inheritance

A class inherits from another class, which inherits from a third class.

```python
class Animal:
    def eat(self):
        return "Eating"

class Mammal(Animal):
    def has_hair(self):
        return "Yes"

class Dog(Mammal):
    def bark(self):
        return "Woof!"
```

### Hierarchical Inheritance

Multiple classes inherit from a single base class.

```python
class Animal:
    def eat(self):
        return "Eating"

class Dog(Animal):
    def bark(self):
        return "Woof!"

class Cat(Animal):
    def meow(self):
        return "Meow!"
```

### Hybrid Inheritance

A combination of multiple, multilevel, and hierarchical inheritance patterns.

```python
class Animal:
    def eat(self):
        return "Eating"

class Mammal(Animal):
    def has_hair(self):
        return "Yes"

class Bird(Animal):
    def fly(self):
        return "Flying"

class Bat(Mammal, Bird):
    def hang(self):
        return "Hanging"
```

## Polymorphism

Polymorphism allows objects of different classes to be treated as objects of a common superclass and enables method redefinition.

### Polymorphism with Class Methods

```python
class Animal:
    def speak(self):
        return "Animal sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow"

def make_animal_speak(animal):
    print(animal.speak())
```

### Polymorphism with Functions and Objects

Functions can work with objects of different classes if they share a common interface.

```python
def describe_animal(animal):
    print(animal.speak())
```

### Overloading

Overloading allows multiple methods or operators to have the same name but different implementations.

### Operator Overloading

Operators can be overloaded to provide custom implementations.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
```

### Magic Methods for Operator Overloading

Magic methods like `__add__`, `__sub__`, etc., are used to overload operators.

### Method Overriding

A method in a derived class overrides a method in its base class.

```python
class Animal:
    def make_sound(self):
        return "Some sound"

class Dog(Animal):
    def make_sound(self):
        return "Woof"
```

### Method Overriding with Multiple and Multilevel Inheritance

```python
class Animal:
    def sound(self):
        return "Some sound"

class Mammal(Animal):
    def sound(self):
        return "Mammal sound"

class Dog(Mammal):
    def sound(self):
        return "Woof"
```

### Constructor Overriding

Derived classes can override the constructor of the base class.

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
```

## Abstraction
Abstraction is the concept of hiding the complex implementation details and showing only the essential features of an object. In Python, this is often achieved using abstract base classes (ABCs) from the abc module.

```python
from abc import ABC, abstractmethod

class AbstractAnimal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Cat(AbstractAnimal):
    def make_sound(self):
        return "Meow"

class Dog(AbstractAnimal):
    def make_sound(self):
        return "Woof"
```
AbstractAnimal is an abstract base class with an abstract method make_sound.  
Cat and Dog provide concrete implementations of the make_sound method.

## Encapsulation

Encapsulation is the bundling of data and methods that operate on the data within a single unit or class. It helps to restrict direct access to some of an object's components, which can prevent accidental modification of data.

### Python Access Modifiers

- **Public**: No restrictions.
- **Protected**: Single underscore (e.g., `_protected`).
- **Private**: Double underscore (e.g., `__private`).

### Why We Need Encapsulation

Encapsulation helps protect an object’s internal state and improves code maintainability and flexibility.

---
&copy; Pranav Mehendale, Yashashri Computers, Kothrud, Pune 2024. All rights reserved. This material is for non-commercial use only.

---