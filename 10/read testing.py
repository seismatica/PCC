filename = "testtext.txt"
with open(filename) as file_object:
    content = file_object.readline(2)
    print(content)