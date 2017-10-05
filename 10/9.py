# Read files containing cats and dogs' name, and print them out.
# If file does not exist, keep silent and process next file.


def print_file(filename):
    try:
        open(filename)
    except FileNotFoundError:
        pass
    else:
        with open(filename) as file_object:
            content = file_object.read()
            print(filename + ": ")
            print(content)


def main():
    filename_list = ["cats.txt", "dogs.txt"]
    for filename in filename_list:
        print_file(filename)


main()