# **Python's `re` Module**

## **1. Introduction to Regular Expressions**

### **What are Regular Expressions (RegEx)?**
Regular expressions are sequences of characters that define search patterns, primarily used for string matching and manipulation. They are incredibly powerful for tasks such as validation, parsing, and transformation of strings.

### **Common Use Cases**
- Validating email addresses, phone numbers, and other inputs.
- Searching and replacing text within documents.
- Extracting specific patterns from large datasets or logs.

## **2. The `re` Module in Python**

### **Overview**
Python provides the `re` module to work with regular expressions. The module contains functions that allow you to perform pattern matching and manipulation efficiently.

### **Basic Syntax and Patterns**

### **Metacharacters in Regular Expressions**
- **`.`**: Matches any character except a newline.
  - Example: `a.b` matches "aab", "a1b", "a@b", etc.
- **`^`**: Matches the start of a string.
  - Example: `^Hello` matches "Hello world" but not "He said Hello".
- **`$`**: Matches the end of a string.
  - Example: `world$` matches "Hello world" but not "worldwide".
- **`*`**: Matches 0 or more repetitions of the preceding element.
  - Example: `ab*` matches "a", "ab", "abb", "abbb", etc.
- **`+`**: Matches 1 or more repetitions of the preceding element.
  - Example: `ab+` matches "ab", "abb", "abbb", but not "a".
- **`?`**: Matches 0 or 1 occurrence of the preceding element.
  - Example: `ab?` matches "a" or "ab".
- **`{n}`**: Matches exactly n occurrences of the preceding element.
  - Example: `a{3}` matches "aaa".
- **`{n,m}`**: Matches between n and m occurrences.
  - Example: `a{2,4}` matches "aa", "aaa", "aaaa".
- **`[]`**: Matches any single character within the brackets.
  - Example: `[abc]` matches "a", "b", or "c".
- **`[^...]`**: Matches any single character not within the brackets.
  - Example: `[^abc]` matches any character except "a", "b", or "c".
- **`|`**: Acts as an OR operator between expressions.
  - Example: `a|b` matches "a" or "b".
- **`()`**: Groups together part of a pattern.
  - Example: `(abc)+` matches "abc", "abcabc", etc.

### **Character Classes**
Character classes allow you to specify a set of characters to match. Some common predefined classes are:
- **`\d`**: Matches any digit (equivalent to `[0-9]`).
- **`\D`**: Matches any non-digit character (equivalent to `[^0-9]`).
- **`\w`**: Matches any word character (equivalent to `[a-zA-Z0-9_]`).
- **`\W`**: Matches any non-word character (equivalent to `[^a-zA-Z0-9_]`).
- **`\s`**: Matches any whitespace character (spaces, tabs, etc.).
- **`\S`**: Matches any non-whitespace character.

### **Core Functions of the `re` Module**

- **`re.match()`**: Checks for a match only at the beginning of the string.
  - Example:
    ```python
    import re
    result = re.match(r'\d+', '123abc')
    print(result.group())  # Output: '123'
    ```
  
- **`re.search()`**: Searches the entire string for the first match.
  - Example:
    ```python
    import re
    result = re.search(r'\d+', 'abc123def')
    print(result.group())  # Output: '123'
    ```

- **`re.findall()`**: Returns all non-overlapping matches of the pattern in the string.
  - Example:
    ```python
    import re
    result = re.findall(r'\d+', 'abc123def456')
    print(result)  # Output: ['123', '456']
    ```

- **`re.finditer()`**: Returns an iterator yielding match objects for all non-overlapping matches.
  - Example:
    ```python
    import re
    result = re.finditer(r'\d+', 'abc123def456')
    for match in result:
        print(match.group())  # Output: '123' and '456'
    ```

- **`re.sub()`**: Replaces occurrences of the pattern with a specified replacement string.
  - Example:
    ```python
    import re
    result = re.sub(r'\d+', '#', 'abc123def456')
    print(result)  # Output: 'abc#def#'
    ```

- **`re.split()`**: Splits the string by the occurrences of the pattern.
  - Example:
    ```python
    import re
    result = re.split(r'\d+', 'abc123def456')
    print(result)  # Output: ['abc', 'def', '']
    ```

## **3. Advanced Features**

### **Lookaheads**

#### **Positive Lookahead (`(?=...)`)**
Asserts that the pattern must be followed by another pattern, without consuming characters.

- **Example**: Match 'foo' only if followed by 'bar'.
  ```python
  import re
  text = "foobar foo baz"
  pattern = r'foo(?=bar)'
  matches = re.findall(pattern, text)
  print(matches)  # Output: ['foo']
  ```

#### **Negative Lookahead (`(?!...)`)**
Asserts that the pattern must NOT be followed by another pattern.

- **Example**: Match 'foo' only if NOT followed by 'bar'.
  ```python
  import re
  text = "foobar foo baz"
  pattern = r'foo(?!bar)'
  matches = re.findall(pattern, text)
  print(matches)  # Output: ['foo']
  ```

### **Lookbehinds**

#### **Positive Lookbehind (`(?<=...)`)**
Asserts that the pattern must be preceded by another pattern.

- **Example**: Match 'bar' only if preceded by 'foo'.
  ```python
  import re
  text = "foobar bazbar"
  pattern = r'(?<=foo)bar'
  matches = re.findall(pattern, text)
  print(matches)  # Output: ['bar']
  ```

#### **Negative Lookbehind (`(?<!...)`)**
Asserts that the pattern must NOT be preceded by another pattern.

- **Example**: Match 'bar' only if NOT preceded by 'foo'.
  ```python
  import re
  text = "foobar bazbar"
  pattern = r'(?<!foo)bar'
  matches = re.findall(pattern, text)
  print(matches)  # Output: ['bar']
  ```

### **Greedy vs. Non-Greedy Matching**

#### **Greedy Matching**
Matches as much of the input string as possible.

- **Example**:
  ```python
  import re
  text = "<p>Paragraph 1</p><p>Paragraph 2</p>"
  pattern_greedy = r'<p>.*</p>'
  matches_greedy = re.findall(pattern_greedy, text)
  print("Greedy:", matches_greedy)  # Output: ['<p>Paragraph 1</p><p>Paragraph 2</p>']
  ```

#### **Non-Greedy Matching**
Matches as little of the input string as possible.

- **Example**:
  ```python
  import re
  text = "<p>Paragraph 1</p><p>Paragraph 2</p>"
  pattern_nongreedy = r'<p>.*?</p>'
  matches_nongreedy = re.findall(pattern_nongreedy, text)
  print("Non-Greedy:", matches_nongreedy)  # Output: ['<p>Paragraph 1</p>', '<p>Paragraph 2</p>']
  ```

### **Grouping and Capturing**

Grouping allows you to segment parts of a regex pattern and capture them for further use.

- **Example**: Extracting the area code and main number from phone numbers.
  ```python
  import re
  text = "Call us at (123) 456-7890 or (987) 654-3210."
  pattern = r'\((\d{3})\)\s(\d{3}-\d{4})'
  matches = re.findall(pattern, text)
  print(matches)  # Output: [('123', '456-7890'), ('987', '654-3210')]
  ```

## **4. Real-Life Use Cases**

### **Use Case 1: Email Address Validation**

#### **Problem Statement**
Validating email addresses in a user registration form to ensure they follow a standard format.

#### **Solution**
- **Pattern**: `^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$`
- **Implementation**:
  ```python
  import re
  
  def validate_email(email):
      pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
      return bool(re.match(pattern, email))
  
  emails = ["user@example.com", "userexample.com", "user@.com"]
  valid_emails = [email for email in emails if validate_email(email)]
  print("Valid emails:", valid_emails)  # Output: ['user@example.com']
  ```

### **Use Case 2: Extracting Phone Numbers from Text**

#### **Problem Statement**
Extracting phone numbers from a text document that contains mixed content.

#### **Solution**
- **Pattern**: `\b\d{3}[-.]?\d{3}[-.]?\d{4}\b`
- **Implementation**:
  ```python
  import re
  text = "Call me at 123-456-7890 or 987.654.3210."
  pattern = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'
  phone_numbers = re.findall(pattern, text)
  print("Phone numbers:", phone_numbers)  # Output: ['123-456-7890', '987.654.3210']
  ```

### **Use Case 3: Splitting a Text Block into Sentences**

#### **Problem Statement**
Breaking down a large block of text into individual sentences.

#### **Solution**
- **Pattern**: `[.!?]\s`
- **Implementation**:
  ```python
  import re
  
  text = "Hello! How are you? I'm fine. Thanks."
  pattern = r'[.!?]\s'
  sentences = re.split(pattern, text)
  print("Sentences:", sentences)  # Output: ['Hello', 'How are you', "I'm fine", 'Thanks.']
  ```

---
&copy; Pranav Mehendale, Yashashri Computers, Kothrud, Pune 2024. All rights reserved. This material is for non-commercial use only.

---