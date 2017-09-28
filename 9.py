def show_magicians(magicians):
    """Receive a list of magicians and print their names"""
    for magician in magicians:
        print(magician.title())


def make_great(magicians):
    """Receive a list of magicians and add "The great" to their names"""
    great_magicians = []
    while magicians:
        magician = magicians.pop()
        great_magician = "The great " + magician
        great_magicians.append(great_magician)
    return great_magicians


magicians = ["David Copperfield", "David Blaine", "Criss Angel"]
great_magicians = make_great(magicians)
show_magicians(great_magicians)