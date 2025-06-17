try:
    file_path = 'd:/Upskillmafia_python/Assignment_4_Files_Exceptions_and_Errors_in_Python/sample.txt'
    with open(file_path, 'r') as file:
        line_no = 1
        for line in file:
            print("line", line_no, ":", line.strip())
            line_no += 1
            
except FileNotFoundError:
    print("Error: sample.txt file not found!")
