# Tuple Operations in Python

## What is a Tuple and How to Create a Tuple

A tuple is an immutable sequence of Python objects. Tuples are similar to lists, but unlike lists, tuples cannot be changed after their creation.

### Creating a Tuple

You can create a tuple by placing a sequence of values separated by commas within parentheses `()`.

```python
# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

# Tuple with mixed data types
mixed_tuple = (1, "Hello", 3.14)
print(mixed_tuple)

# Creating a tuple without parentheses (tuple packing)
packed_tuple = 1, 2, 3
print(packed_tuple)

# Creating a tuple with a single element (note the comma)
single_element_tuple = (1,)
print(single_element_tuple)
```

## Accessing Tuple

You can access elements in a tuple using indexing and slicing, similar to lists.

```python
# Accessing elements
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[0])  # Output: 1
print(my_tuple[1:3])  # Output: (2, 3)
print(my_tuple[-1])  # Output: 5

# Nested tuple
nested_tuple = ("Hello", [1, 2, 3], (4, 5, 6))
print(nested_tuple[1])  # Output: [1, 2, 3]
print(nested_tuple[2][1])  # Output: 5
```

## Mathematical Operators for Tuple

Tuples support concatenation and repetition operators.

```python
# Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)  # Output: (1, 2, 3, 4, 5, 6)

# Repetition
repeated_tuple = tuple1 * 3
print(repeated_tuple)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)
```

## Functions of Tuple

Tuples have several built-in functions.

```python
my_tuple = (1, 2, 3, 4, 5)

# len() - returns the number of elements in a tuple
print(len(my_tuple))  # Output: 5

# max() - returns the largest element in a tuple
print(max(my_tuple))  # Output: 5

# min() - returns the smallest element in a tuple
print(min(my_tuple))  # Output: 1

# sum() - returns the sum of all elements in a tuple
print(sum(my_tuple))  # Output: 15

# count() - returns the number of occurrences of a specified element
print(my_tuple.count(3))  # Output: 1

# index() - returns the index of the first occurrence of a specified element
print(my_tuple.index(4))  # Output: 3
```

## Tuple Packing and Unpacking

### Packing

Packing refers to the assignment of multiple values to a tuple.

```python
# Tuple packing
packed_tuple = 1, "Hello", 3.14
print(packed_tuple)  # Output: (1, 'Hello', 3.14)
```

### Unpacking

Unpacking refers to the extraction of values from a tuple into individual variables.

```python
# Tuple unpacking
my_tuple = (1, "Hello", 3.14)
a, b, c = my_tuple
print(a)  # Output: 1
print(b)  # Output: Hello
print(c)  # Output: 3.14
```

## Tuple Comprehension

Tuples do not support comprehension directly as lists do, but you can use generator expressions that look similar to tuple comprehension.

```python
# Generator expression (similar to tuple comprehension)
generator = (x**2 for x in range(5))

# Converting generator to tuple
tuple_comprehension = tuple(generator)
print(tuple_comprehension)  # Output: (0, 1, 4, 9, 16)
```

## Difference Between List and Tuple

| Feature              | List                                  | Tuple                                 |
|----------------------|---------------------------------------|---------------------------------------|
| **Mutability**       | Mutable (can be modified)             | Immutable (cannot be modified)        |
| **Syntax**           | Defined using square brackets `[]`    | Defined using parentheses `()`        |
| **Performance**      | Slower due to overhead of mutability  | Faster due to immutability            |
| **Methods**          | Has more built-in methods for operations | Has fewer built-in methods            |
| **Use Case**         | Suitable for collections that may change | Suitable for fixed collections        |
| **Memory Usage**     | Generally uses more memory            | Generally uses less memory            |
| **Iteration**        | Slower iteration                      | Faster iteration                      |

### Examples

```python
# List example (mutable)
my_list = [1, 2, 3]
my_list[0] = 4
print(my_list)  # Output: [4, 2, 3]

# Tuple example (immutable)
my_tuple = (1, 2, 3)
# my_tuple[0] = 4  # This will raise a TypeError
```

### Performance

```python
import timeit

# Performance comparison
list_time = timeit.timeit(stmt="[1, 2, 3, 4, 5]", number=1000000)
tuple_time = timeit.timeit(stmt="(1, 2, 3, 4, 5)", number=1000000)

print(f"List time: {list_time}")
print(f"Tuple time: {tuple_time}")
```
---
&copy; Pranav Mehendale, Yashashri Computers, Kothrud, Pune 2024. All rights reserved. This material is for non-commercial use only.

---
