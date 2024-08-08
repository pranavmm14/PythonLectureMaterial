## Application of Dictionaries

### Easy

#### 1. Counting Word Frequency
Given a string `text`, create a dictionary that counts the frequency of each word. Ignore punctuation and case.

```python
text = "This is a sentence with no punctuation it is very long and it repeats words it is a long sentence with no punctuation and it keeps going on and on it is a very very long sentence it has no punctuation and it just keeps repeating words and it goes on and on without stopping it is a very long sentence and it does not make sense but it is long and has no punctuation and it repeats words over and over again it just keeps going on and on with no punctuation and it is very long and repetitive"
# Your code here to create the dictionary `word_freq`
```

**Hint:** Convert the text to lowercase, remove punctuation, split into words, and count occurrences.

### Medium

#### 2. Student Grades
Create a dictionary `student_grades` that stores the names of students and their grades in a subject. Calculate the average grade of the students.

```python
student_grades = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "David": 88,
    "Eva": 91
}
# Your code here to calculate the average grade
```

**Hint:** Use the `sum` function and `len` function to calculate the average.

#### 3. Inventory Management
Create a dictionary `inventory` that stores item names and their quantities. Perform the following actions:
- Add 12 pears to the inventory
- Remove bananas from the inventory
- Update the quantity of oranges to 10

```python
inventory = {
    "apple": 10,
    "banana": 5,
    "orange": 8
}
# Your code here to update the inventory
```

**Hint:** Use dictionary methods to add, update, and delete items.

### Hard

#### 4. Employee Directory
Create a dictionary `employee_directory` that stores employee IDs as keys and dictionaries as values. Each nested dictionary should contain the employee's name, position, and salary. Perform the following actions:
- Add an employee with ID 104, name David, position Tester, and salary 55000
- Update the salary of employee with ID 102 to 70000
- Remove the employee with ID 103

```python
employee_directory = {
    101: {"name": "Alice", "position": "Manager", "salary": 75000},
    102: {"name": "Bob", "position": "Developer", "salary": 65000},
    103: {"name": "Charlie", "position": "Designer", "salary": 60000}
}
# Your code here to update the employee directory
```

**Hint:** Use nested dictionaries and perform add, update, and delete operations.

#### 5. Course Enrollment
Create a dictionary `course_enrollment` where the keys are course names and the values are lists of student names enrolled in those courses. Perform the following actions:
- Add Eva to the Math course
- Remove David from the Science course
- List all students in the Math course

```python
course_enrollment = {
    "Math": ["Alice", "Bob"],
    "Science": ["Charlie", "David"],
    "History": ["Eva"]
}
# Your code here to update the course enrollment
```

**Hint:** Use list methods to add and remove students from the course lists.

### Challenging

#### 6. Airline Reservation System
Create a dictionary `flights` where keys are flight numbers and values are dictionaries with keys "destination", "departure_time", and "seats". Perform the following actions:
- Book a seat on flight AA101 (decrease seats by 1)
- Cancel a booking on flight BA202 (increase seats by 1)
- Update the number of seats on flight CA303 to 85

```python
flights = {
    "AA101": {"destination": "New York", "departure_time": "10:00 AM", "seats": 100},
    "BA202": {"destination": "London", "departure_time": "12:00 PM", "seats": 80},
    "CA303": {"destination": "Paris", "departure_time": "02:00 PM", "seats": 90}
}
# Your code here to update the airline reservation system
```

**Hint:** Use dictionary methods to update the number of seats by performing arithmetic operations.

---

## Hints

### 1. Counting Word Frequency
- Convert the text to lowercase using `lower()`.
- Split the text into words using `split()`.
- Use a loop to count word occurrences and store them in a dictionary.

### 2. Student Grades
- Use `sum()` to get the total of all grades.
- Use `len()` to get the number of students.
- Calculate the average by dividing the total by the number of students.

### 3. Inventory Management
- Use dictionary assignment to add and update items.
- Use `del` to remove items from the dictionary.

### 4. Employee Directory
- Use dictionary assignment to add new employee entries.
- Access nested dictionary values to update employee details.
- Use `del` to remove employees from the directory.

### 5. Course Enrollment
- Use the `append()` method to add students to the course lists.
- Use the `remove()` method to remove students from the course lists.
- Access the list of students for a specific course.

### 6. Airline Reservation System
- Decrease the number of seats using `-= 1`.
- Increase the number of seats using `+= 1`.
- Update the value of seats directly by assigning a new number.

---
&copy; Pranav Mehendale, Yashashri Computers, Kothrud, Pune 2024. All rights reserved. This material is for non-commercial use only.

---
