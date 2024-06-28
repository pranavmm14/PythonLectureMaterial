# List Operations in Python

## 1. What is a List and its Creation

A list in Python is a collection of items which are ordered and changeable. Lists are written with square brackets `[]`.

```python
# List creation
my_list = [1, 2, 3, 4, 5]
print("List:", my_list)
```
In the example above, my_list is a list containing the integers 1 through 5.

## 2. Accessing Elements of List
You can access elements of a list by their index. Indexing starts from 0.

```python
# Accessing elements
print("First element:", my_list[0])
print("Last element:", my_list[-1])
```
Here, my_list[0] accesses the first element, and my_list[-1] accesses the last element.

## 3. Mutability and Immutability
Lists are mutable, meaning their elements can be changed.

```python
# Mutability
my_list[2] = 10
print("After modification:", my_list)
```
In this example, the third element of my_list is changed from 3 to 10.

## 4. List Traversing
You can traverse a list using a loop.

```python
# List Traversing
for item in my_list:
    print(item)
```
This loop prints each element of my_list.

## 5. Functions of List - Get Information about List
Python lists have various functions to get information about them.

```python
# Getting information about list
print("Length of list:", len(my_list))
print("Max value in list:", max(my_list))
print("Min value in list:", min(my_list))
print("Sum of list:", sum(my_list))
```
- len(my_list) returns the number of elements in the list.
- max(my_list) returns the maximum value in the list.
- min(my_list) returns the minimum value in the list.
- sum(my_list) returns the sum of all elements in the list.

## 6. Manipulating List
You can manipulate lists by adding, removing, or modifying elements.

```python
# Adding elements
my_list.append(6)
print("After appending 6:", my_list)

# Inserting elements
my_list.insert(1, 7)
print("After inserting 7 at index 1:", my_list)

# Removing elements
my_list.remove(10)
print("After removing 10:", my_list)

# Popping elements
popped = my_list.pop()
print("After popping last element:", my_list)
print("Popped element:", popped)
```
- append(6) adds 6 to the end of the list.
- insert(1, 7) inserts 7 at index 1.
- remove(10) removes the first occurrence of 10.
- pop() removes and returns the last element.

## 7. Ordering Elements of List

Lists can be sorted in ascending or descending order.
```python
# Sorting list
my_list.sort()
print("Sorted list:", my_list)

# Reversing list
my_list.reverse()
print("Reversed list:", my_list)
```
- sort() sorts the list in ascending order.\
- reverse() reverses the order of the list.

## 8. Iterative Statement
Using iterative statements with lists.

```python
# Using for loop to print list elements
for i in range(len(my_list)):
    print(my_list[i])
```
This loop iterates over each element in the list and prints it.

## 9. Use of Mathematical Operators for List
Applying mathematical operations on lists.

```python

# List mathematical operations
another_list = [2, 4, 6, 8]
summed_list = [x + y for x, y in zip(my_list, another_list)]
print("Sum of elements of two lists:", summed_list)

# Multiplying list elements by a constant
multiplied_list = [x * 2 for x in my_list]
print("List after multiplying each element by 2:", multiplied_list)
```
- zip(my_list, another_list) combines elements from two lists.
- The list comprehension [x + y for x, y in zip(my_list, another_list)] sums corresponding elements from the lists.
- [x * 2 for x in my_list] multiplies each element by 2.

## 10. Comparison and Membership Operators
Using comparison and membership operators with lists.

```python
# Comparison operators
print("Is my_list equal to another_list?", my_list == another_list)

# Membership operators
print("Is 2 in my_list?", 2 in my_list)
print("Is 10 not in my_list?", 10 not in my_list)
```
- my_list == another_list checks if the two lists are equal.
- 2 in my_list checks if 2 is an element of my_list.
- 10 not in my_list checks if 10 is not an element of my_list.

## 11. Nested List
Lists can contain other lists as elements, creating a nested list.

```python
# Nested list
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Nested list:", nested_list)

# Accessing elements in nested lists
print("First sublist:", nested_list[0])
print("Element of first sublist:", nested_list[0][1])
```
- nested_list is a list of lists.
- nested_list[0] accesses the first sublist.
- nested_list[0][1] accesses the second element of the first sublist.

## 12. List Comprehension
List comprehensions provide a concise way to create lists.

```python
# List comprehension
squares = [x**2 for x in range(10)]
print("Squares of numbers 0-9:", squares)

# List comprehension with condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print("Squares of even numbers 0-9:", even_squares)
```
- [x ** 2 for x in range(10)] creates a list of squares of numbers from 0 to 9.
- [x ** 2 for x in range(10) if x % 2 == 0] creates a list of squares of even numbers from 0 to 9.

---
&copy; Pranav Mehendale, Yashashri Computers, Kothrud, Pune 2024. All rights reserved. This material is for non-commercial use only.

---