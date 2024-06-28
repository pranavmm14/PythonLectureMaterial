# Python Sets and Operations

## Introduction

A **set** is an unordered collection of unique elements. Sets are mutable, meaning you can add or remove elements from a set after it is created, but the elements themselves must be immutable (like strings, numbers, or tuples).

## Creating Sets

You can create a set using curly braces `{}` or the `set()` function.

```python
# Using curly braces
my_set = {1, 2, 3, 4}
print(my_set)  # Output: {1, 2, 3, 4}

# Using the set() function
my_set = set([1, 2, 3, 4])
print(my_set)  # Output: {1, 2, 3, 4}

# Creating an empty set
empty_set = set()
print(empty_set)  # Output: set()

s1 = {[1,2,3],4,"hi"} #Gives Error
```
```shell
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    s1 = {[1,2,3],4,"hi"}
TypeError: unhashable type: 'list'
```

## Modifying Sets

You can add elements to a set using the `add()` method and remove elements using the `remove()` or `discard()` methods.

```python
my_set = {1, 2, 3}

# Adding an element
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}
```

## Removing Elements from a Set

You can remove elements from a set using the `remove()` or `discard()` methods. To remove all elements, use the `clear()` method.

```python
my_set = {1, 2, 3, 4}

# Removing an element
my_set.remove(2)
print(my_set)  # Output: {1, 3, 4}

# Discarding an element (won't raise an error if the element is not found)
my_set.discard(5)
print(my_set)  # Output: {1, 3, 4}

# Removing all elements
my_set.clear()
print(my_set)  # Output: set()
```

## Python Set Operations

Sets support various mathematical operations like union, intersection, difference, and symmetric difference.

### Union

The union of two sets is a set containing all elements from both sets.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1.union(set2)
# or
union_set = set1 | set2
print(union_set)  # Output: {1, 2, 3, 4, 5}
```

### Intersection

The intersection of two sets is a set containing only the elements that are in both sets.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

intersection_set = set1.intersection(set2)
# or
intersection_set = set1 & set2
print(intersection_set)  # Output: {3}
```

### Difference

The difference of two sets is a set containing the elements of the first set that are not in the second set.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

difference_set = set1.difference(set2)
# or
difference_set = set1 - set2
print(difference_set)  # Output: {1, 2}
```

### Symmetric Difference

The symmetric difference of two sets is a set containing the elements that are in either of the sets but not in both.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

symmetric_difference_set = set1.symmetric_difference(set2)
# or
symmetric_difference_set = set1 ^ set2
print(symmetric_difference_set)  # Output: {1, 2, 4, 5}
```

## Set Methods

### Adding and Removing Elements

- **`add()`**: Adds an element to the set.
- **`remove()`**: Removes a specified element from the set. Raises a KeyError if the element is not found.
- **`discard()`**: Removes a specified element from the set. Does not raise an error if the element is not found.
- **`clear()`**: Removes all elements from the set.

### Copying a Set

- **`copy()`**: Returns a shallow copy of the set.

### Checking Subsets and Supersets

- **`issubset(other_set)`**: Returns `True` if the set is a subset of `other_set`.
- **`issuperset(other_set)`**: Returns `True` if the set is a superset of `other_set`.

### Checking for Disjoint Sets

- **`isdisjoint(other_set)`**: Returns `True` if the set has no elements in common with `other_set`.

```python
my_set = {1, 2, 3}

# Copying a set
new_set = my_set.copy()
print(new_set)  # Output: {1, 2, 3}

# Checking subsets and supersets
subset = {1, 2}
print(subset.issubset(my_set))  # Output: True
print(my_set.issuperset(subset))  # Output: True

# Checking disjoint sets
disjoint_set = {4, 5, 6}
print(my_set.isdisjoint(disjoint_set))  # Output: True
```

## Built-in Functions

- **`len()`**: Returns the number of elements in a set.
- **`in`**: Checks if an element is in the set.

```python
my_set = {1, 2, 3}

print(len(my_set))  # Output: 3
print(2 in my_set)  # Output: True
print(4 in my_set)  # Output: False
```

## Set Comprehension

Set comprehensions are similar to list comprehensions but use curly braces `{}`.

```python
# Example of set comprehension
squared_set = {x**2 for x in range(10)}
print(squared_set)  # Output: {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}
```

## Frozen Sets

A frozenset is an immutable version of a set. Once created, elements cannot be added or removed.

```python
# Creating a frozenset
fs = frozenset([1, 2, 3, 4])
print(fs)  # Output: frozenset({1, 2, 3, 4})

# Frozenset operations (similar to sets)
print(fs.union({5, 6}))  # Output: frozenset({1, 2, 3, 4, 5, 6})
print(fs.intersection({2, 3, 5}))  # Output: frozenset({2, 3})
```

---

&copy; Pranav Mehendale, Yashashri Computers, Kothrud, Pune 2024. All rights reserved. This material is for non-commercial use only.

---
