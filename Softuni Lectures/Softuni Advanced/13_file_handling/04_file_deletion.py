import os

try:
    path = os.path.join("my_first_file.txt")
    os.remove(path)
except FileNotFoundError:
    print("File is already deleted")
