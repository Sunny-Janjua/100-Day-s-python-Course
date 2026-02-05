# import os

# print(os.getcwd())

# folder_name = "sunny"

# # check if folder already exists
# if not os.path.exists(folder_name):
#     os.mkdir(folder_name)
#     print(f"Folder '{folder_name}' created")
# else:
#     print(f"Folder '{folder_name}' already exists")

# # create single folder
# if not os.path.exists("test_folder"):
#     os.mkdir("test_folder")

# # create nested folders
# os.makedirs("a/b/c", exist_ok=True)

# import os

# for i in range(101):
#     old_name = f"sunny/main{i}"
#     new_name = f"sunny/newMain{i}"

#     if os.path.exists(old_name):
#         os.rename(old_name, new_name)

# print(dir(os))

# file = open("main.py", "r")

# for line in file:
#     print(line)

# file.close()

# file = open("sunny.txt", "w")
# file.write("Hello Sunny\n")
# file.write("Python File Handling\n")
# file.close()

# file = open("newfile.txt", "x")
# file.write("File created")
# file.close()


with open("image.png", "rb") as file:
    data = file.read()
    print(data)
