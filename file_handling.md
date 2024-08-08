# Python File and Directory Operations

## Open File
Opening a file in Python is done using the `open()` function, which returns a file object. The basic syntax is:
```python
file_object = open('filename', 'mode')
```
- `filename` is the name of the file to open.
- `mode` is a string indicating how the file is to be opened:
  - `'r'`: Read (default)
  - `'w'`: Write (truncates the file if it exists)
  - `'a'`: Append
  - `'b'`: Binary mode
  - `'t'`: Text mode (default)
  - `'+'`: Read and write

### Example
```python
file = open('example.txt', 'r')
```

## Properties of Files
Once a file is opened, you can access several properties:
- `file.name`: Name of the file.
- `file.mode`: Mode in which the file is opened.
- `file.closed`: Boolean indicating whether the file is closed.

### Example
```python
print(file.name)
print(file.mode)
print(file.closed)
```

## Read & Write Operation
Reading and writing to a file can be done using various methods:
- `file.read(size)`: Reads up to `size` bytes from the file.
- `file.readline()`: Reads a single line from the file.
- `file.readlines()`: Reads all lines in a file and returns them as a list.
- `file.write(string)`: Writes `string` to the file.
- `file.writelines(list)`: Writes a list of strings to the file.

### Example
```python
with open('example.txt', 'w') as file:
    file.write('Hello, World!')

with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
```

## Seek and Tell Method
- `file.seek(offset, whence)`: Moves the file pointer to a specified location.
  - `offset` is the number of bytes to move.
  - `whence` is optional and defaults to 0 (beginning of the file). Other values: 1 (current position), 2 (end of the file).
- `file.tell()`: Returns the current file pointer position.

### Example
```python
with open('example.txt', 'r') as file:
    print(file.tell())
    file.seek(5)
    print(file.read())
```

## OS Module
The `os` module provides a way to interact with the operating system.
- `os.name`: Name of the operating system dependent module imported.
- `os.getcwd()`: Returns the current working directory.
- `os.listdir(path)`: Returns a list of entries in the directory given by `path`.
- `os.mkdir(path)`: Creates a directory named `path`.
- `os.remove(path)`: Removes the file path.
- `os.rmdir(path)`: Removes the directory path.

### Example
```python
import os

print(os.name)
print(os.getcwd())
os.mkdir('new_directory')
print(os.listdir('.'))
os.rmdir('new_directory')
```

## Working with Directories
Using the `os` and `os.path` modules, you can work with directories:
- `os.path.exists(path)`: Returns `True` if `path` exists.
- `os.path.join(path, *paths)`: Joins one or more path components.
- `os.path.basename(path)`: Returns the base name of `path`.
- `os.path.dirname(path)`: Returns the directory name of `path`.

### Example
```python
import os

if not os.path.exists('example_directory'):
    os.mkdir('example_directory')

print(os.path.join('example_directory', 'file.txt'))
```

## Handling Binary Data
Files can be opened in binary mode using the `b` mode. This is useful for non-text files.
### Example
```python
with open('example.bin', 'wb') as file:
    file.write(b'\x00\xFF\x00\xFF')
    
with open('example.bin', 'rb') as file:
    data = file.read()
    print(data)
```

## CSV Files
The `csv` module is used to handle CSV files.
- `csv.reader(file)`: Reads from a CSV file.
- `csv.writer(file)`: Writes to a CSV file.
- `csv.DictReader(file)`: Reads from a CSV file into a dictionary.
- `csv.DictWriter(file, fieldnames)`: Writes to a CSV file from a dictionary.

### Example
```python
import csv

with open('example.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age'])
    writer.writerow(['Alice', 30])
    writer.writerow(['Bob', 25])

with open('example.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

## Zip and Unzip
The `zipfile` module allows you to work with ZIP archives.
- `zipfile.ZipFile(file, mode)`: Opens a ZIP file.
- `ZipFile.write(filename)`: Adds a file to the archive.
- `ZipFile.extract(member, path)`: Extracts a member from the archive.

### Example
```python
import zipfile

with zipfile.ZipFile('example.zip', 'w') as zipf:
    zipf.write('example.txt')

with zipfile.ZipFile('example.zip', 'r') as zipf:
    zipf.extractall('extracted_files')
```
&copy; Pranav Mehendale, Yashashri Computers, Kothrud, Pune 2024. All rights reserved. This material is for non-commercial use only.

---