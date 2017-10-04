# Read files containing cats and dogs' name, and print them out. If file does not exist, print error

cats_file = "cats.txt"
dogs_file = "dogs.txt"


def print_file(filename):
    try:
        open(filename)
    except FileNotFoundError:
        print(filename + " not found.")
    else:
        with open(filename) as file_object:
            content = file_object.read()
            print(filename + ": ")
            print(content)


print_file(cats_file)
print_file(dogs_file)