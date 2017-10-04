# Prompt users to enter two numbers and add them. If user enters a text, print an error message


def main():
    while True:
        try:
            x = input("Input your first number (type 'q' to quit): ")
            if x == 'q':
                break
            x_float = float(x)

            y = input("Input your second number (type 'q' to quit): ")
            if y == 'q':
                break
            y_float = float(y)
        except ValueError:
            print("You did not enter a number. Please try again")
        else:
            z = x_float + y_float
            print("The sum of your numbers is " + str(z))


main()
