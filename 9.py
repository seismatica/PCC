def show_magicians(magicians):
    """Receive a list of magicians and print their names"""
    for magician in magicians:
        print(magician.title())


def make_great(magicians):
    """Receive a list of magicians and add "The great" to their names"""
    for i in range(len(magicians)):
        magicians[i] = "The great " + magicians[i]  # modify list elements in place using index


magicians = ["David Copperfield", "David Blaine", "Criss Angel"]
make_great(magicians)
print(magicians)