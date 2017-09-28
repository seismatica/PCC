def show_magicians(magicians):
    """Receive a list of magician and print their names"""
    for magician in magicians:
        print(magician.title())


magicians = ["David Copperfield", "David Blaine", "Criss Angel"]
show_magicians(magicians)