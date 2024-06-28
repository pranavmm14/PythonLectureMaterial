# Python List Operations Assignment No. 3



&copy; Pranav Mehendale, Yashashri Computers, Kothrud, Pune 2024. All rights reserved. This material is for non-commercial use only.

---

### Question 1: List Creation and Accessing Elements
Create a list of the first 10 positive integers. Write code to:
1. Print the entire list.
2. Print the first and last elements of the list.
3. Print the element at the 5th index.

```python
# Solution for Question 1
integers = list(range(1, 11))
print("List of first 10 positive integers:", integers)
print("First element:", integers[0])
print("Last element:", integers[-1])
print("Element at the 5th index:", integers[5])
```

---

### Question 2: Mutability of Lists
Given the list `numbers = [10, 20, 30, 40, 50]`:
1. Change the second element to 25.
2. Change the last element to 55.
3. Print the modified list.

```python
# Solution for Question 2
numbers = [10, 20, 30, 40, 50]
numbers[1] = 25
numbers[-1] = 55
print("Modified list:", numbers)
```

---

### Question 3: List Traversing
Write a program to traverse the list `fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']` and print each fruit in uppercase.

```python
# Solution for Question 3
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
for fruit in fruits:
    print(fruit.upper())
```

---

### Question 4: List Functions
Given the list `data = [5, 3, 8, 6, 7, 2]`, write code to:
1. Find and print the length of the list.
2. Find and print the maximum and minimum values in the list.
3. Calculate and print the sum of all elements in the list.

```python
# Solution for Question 4
data = [5, 3, 8, 6, 7, 2]
print("Length of the list:", len(data))
print("Maximum value in the list:", max(data))
print("Minimum value in the list:", min(data))
print("Sum of all elements in the list:", sum(data))
```

---

### Question 5: List Manipulation and Conditions
Given the list `scores = [85, 62, 75, 90, 88, 76, 95, 89, 60, 77]`, write code to:
1. Add a new score 82 at the end of the list.
2. Remove all scores less than 70.
3. Print the updated list.
4. Check if the score 95 is in the list and print an appropriate message.

```python
# Solution for Question 5
scores = [85, 62, 75, 90, 88, 76, 95, 89, 60, 77]
scores.append(82)
scores = [score for score in scores if score >= 70]
print("Updated list of scores:", scores)
if 95 in scores:
    print("Score 95 is in the list")
else:
    print("Score 95 is not in the list")
```

---

### Question 6: Sorting and Reversing a List
Create a list of 7 random integers. Write code to:
1. Sort the list in ascending order and print it.
2. Reverse the list and print it.

```python
# Solution for Question 6
random_integers = [85, 62, 75, 90, 88, 76, 95, 89, 60, 77]
print("Original list:", random_integers)
random_integers.sort()
print("Sorted list:", random_integers)
random_integers.reverse()
print("Reversed list:", random_integers)
```

---

### Question 7: List Comprehensions and Nested Lists
1. Use list comprehensions to create a list of squares of the first 10 positive integers.
2. Create a nested list where each sublist contains the square and cube of numbers from 1 to 5. Print the nested list.

```python
# Solution for Question 7
squares = [x**2 for x in range(1, 11)]
print("Squares of the first 10 positive integers:", squares)

nested_list = [[x, x**2, x**3] for x in range(1, 6)]
print("Nested list of squares and cubes from 1 to 5:", nested_list)
```

---

### Question 8: Advanced Application
Given the list `temperatures = [72, 68, 75, 70, 69, 80, 78, 74, 73, 71]`, write code to:
1. Calculate and print the average temperature.
2. Create a new list that contains only the temperatures that are above the average temperature.
3. Print the list of temperatures above average.

```python
# Solution for Question 8
temperatures = [72, 68, 75, 70, 69, 80, 78, 74, 73, 71]
average_temperature = sum(temperatures) / len(temperatures)
print("Average temperature:", average_temperature)

above_average_temperatures = [temp for temp in temperatures if temp > average_temperature]
print("Temperatures above average:", above_average_temperatures)
```


### Question 9: Sales Data Analysis

You have monthly sales data for a store. Your task is to analyze this data:

1. Create a list of monthly sales data.
2. Calculate and print the total sales for the year.
3. Calculate and print the average monthly sales.
4. Find and print the month with the highest sales.
5. Find and print the month with the lowest sales.
6. Print the names of all months where sales were above the average monthly sales.

**Example Input:**
```python
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
sales = [1200, 1500, 1100, 1800, 2300, 2200, 1700, 2100, 1600, 1900, 2000, 2500]
```

**Solution:**

```python
# Calculate total sales for the year
total_sales = sum(sales)
print("Total sales for the year:", total_sales)

# Calculate average monthly sales
average_sales = total_sales / len(sales)
print("Average monthly sales:", average_sales)

# Find the month with the highest sales
highest_sales = max(sales)
highest_sales_month = months[sales.index(highest_sales)]
print("Month with the highest sales:", highest_sales_month)

# Find the month with the lowest sales
lowest_sales = min(sales)
lowest_sales_month = months[sales.index(lowest_sales)]
print("Month with the lowest sales:", lowest_sales_month)

# Print the names of all months with sales above average
print("Months with sales above average:")
for i in range(len(sales)):
    if sales[i] > average_sales:
        print(months[i])
```

---

## Question 10: Movie Ratings Analysis

You have data on movie ratings given by a group of friends. Each friend rates several movies on a scale from 1 to 10. Your task is to analyze this data:

1. Create a list of movie ratings for each friend.
2. Calculate and print the total number of ratings given by all friends.
3. Calculate and print the average rating for each movie.
4. Identify and print the highest rating for each movie.
5. Identify and print the lowest rating for each movie.
6. Count and print the number of movies that have an average rating of 8 or above.

**Example Input:**
```python
friends = ["Ravi", "Sita", "Amit", "Priya", "Rahul"]
ratings = [
    [8, 7, 9, 6, 8],  # Ravi's ratings
    [7, 8, 7, 5, 6],  # Sita's ratings
    [8, 9, 8, 7, 9],  # Amit's ratings
    [6, 6, 7, 8, 7],  # Priya's ratings
    [9, 8, 7, 9, 8]   # Rahul's ratings
]
```

**Solution:**

```python
# Calculate total number of ratings given by all friends
total_ratings = sum(len(friend_ratings) for friend_ratings in ratings)
print("Total number of ratings given by all friends:", total_ratings)

# Calculate average rating for each movie
num_movies = len(ratings[0])
average_ratings = []
for i in range(num_movies):
    total_rating_for_movie = sum(friend_ratings[i] for friend_ratings in ratings)
    average_ratings.append(total_rating_for_movie / len(friends))

print("Average ratings for each movie:", average_ratings)

# Identify the highest rating for each movie
highest_ratings = []
for i in range(num_movies):
    highest_rating_for_movie = max(friend_ratings[i] for friend_ratings in ratings)
    highest_ratings.append(highest_rating_for_movie)

print("Highest ratings for each movie:", highest_ratings)

# Identify the lowest rating for each movie
lowest_ratings = []
for i in range(num_movies):
    lowest_rating_for_movie = min(friend_ratings[i] for friend_ratings in ratings)
    lowest_ratings.append(lowest_rating_for_movie)

print("Lowest ratings for each movie:", lowest_ratings)

# Count the number of movies with an average rating of 8 or above
highly_rated_movies_count = sum(1 for rating in average_ratings if rating >= 8)
print("Number of movies with an average rating of 8 or above:", highly_rated_movies_count)
```

---
