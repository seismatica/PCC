filename = "learning_python.txt"
with open(filename) as file_object:
    # 1: Read file directly
    # print(file_object.read())
    #
    # 2: Loop over the file object directly
    # for line in file_object:
    #     print(line.rstrip())
    #
    # 3: Break file down to lines stored in list, and print these lines from the list
    line_list = file_object.readlines()
    display = ""

# print(line_list)
for line in line_list:
    line = line.replace('Python', 'Java')
    display += line
print(display)