file_path = input().split("\\")
filename_and_extension = file_path[-1]
filename, extension = filename_and_extension.split(".")
print(f"File name: {filename}")
print(f"File extension: {extension}")