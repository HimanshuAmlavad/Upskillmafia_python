# Assignment 4 - Files, Exceptions, and Errors in Python

This assignment demonstrates file handling and error management in Python through two practical tasks.

---

## Task 1: Read a File and Handle Errors

**File:** `Task_1.py`

- Opens and reads the contents of a text file (`sample.txt`).
- Prints each line of the file to the console.
- Handles errors gracefully if the file does not exist or cannot be read.

**Example Output:**
```
Line 1: This is the first line.
Line 2: This is the second line.
...
```
If the file is missing:
```
Error: sample.txt file not found!
```

---

## Task 2: Write and Append Data to a File

**File:** `Task_2.py`

- Takes user input and writes it to a file named `output.txt`.
- Appends additional user input to the same file.
- Reads and displays the final content of the file.
- Handles file I/O errors gracefully.

**Example Usage:**
```
Enter text to write to file: Hello, world!
Initial content written to file successfully!
Enter additional text to append: This is a new line.
Additional content appended successfully!

Final content of the file:
--------------------------
Hello, world!
This is a new line.
```

---

## Concepts Covered

- File reading and writing (`open`, `read`, `write`, `append`)
- Using context managers (`with` statement)
- Exception handling with `try-except`
- User input and output
- Error messages for missing files or I/O issues

---

**Requirements:**  
- Python 3.x  
- The script files and text files should be in the same directory for easy