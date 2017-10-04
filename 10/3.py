# Prompt users for their name, and store the responses to a file called guest.txt

filename = "guest.txt"

with open(filename, "w") as file_object:
    file_object.write("---Guest list---\n")
    while True:
        guest_name = input("Please enter your first name (type 'q' to quit): ")
        if guest_name == 'q':
            break
        file_object.write(guest_name + "\n")