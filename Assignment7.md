# Assignment: File and Directory Operations and Functions in Python

### Functions

#### Task 1: Basic Function and File Handling
1. Create a text file named `greetings.txt` and write the following names to it:
    ```
    Alice
    Bob
    Charlie
    ```
2. Write a function `greet(name)` that:
    - Takes a name as an argument.
    - Returns a greeting message "Hello, `name`!".
3. Write a Python script that:
    - Opens `greetings.txt` and reads the names line by line.
    - Uses the `greet` function to generate a greeting for each name.
    - Writes each greeting to a new file named `greetings_output.txt`.

#### Task 2: Lambda Function and Map
1. Create a list of numbers `[1, 2, 3, 4, 5]`.
2. Write a lambda function `square` that:
    - Takes a number as input.
    - Returns the square of the number.
3. Write a Python script that:
    - Uses the `map` function to apply the `square` lambda function to the list of numbers.
    - Writes the squared numbers to a file named `squared_numbers.txt`.

#### Task 3: Filter Even Numbers and Write to File
1. Write a function `filter_even_numbers(numbers)` that:
    - Takes a list of numbers.
    - Returns a list of even numbers using the `filter` function.
2. Create a list of numbers `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`.
3. Write a Python script that:
    - Uses the `filter_even_numbers` function to get even numbers from the list.
    - Writes the even numbers to a file named `even_numbers.txt`.

### File Handling

#### Task 4: Open, Read, and Close a File
1. Create a text file named `testfile.txt` and write the following lines to it:
    ```
    Hello, this is a test file.
    It contains multiple lines.
    Let's read it using Python.
    ```
2. Write a Python script to:
    - Open the file in read mode.
    - Print its contents line by line.
    - Close the file.

#### Task 5: Seek and Tell
1. Using the `testfile.txt` file from Task 4, write a Python script to:
    - Open the file in read mode.
    - Print the current file pointer position.
    - Move the file pointer to the beginning of the file.
    - Read and print the first 10 characters.
    - Move the file pointer to the end of the file.
    - Print the current file pointer position.
    - Close the file.

#### Task 6: Using the OS Module
1. Write a Python script to perform the following operations:
    - Print the current working directory.
    - Create a new directory named `test_directory`.
    - List all entries in the current working directory.
    - Remove the `test_directory`.

#### Task 7: Working with CSV Files
1. Create a CSV file named `data.csv` with the following content:
    ```
    Name, Age
    Alice, 30
    Bob, 25
    Charlie, 35
    ```
2. Write a Python script to:
    - Read the contents of `data.csv` and print each row.
    - Add a new row `David, 40` to `data.csv`.
