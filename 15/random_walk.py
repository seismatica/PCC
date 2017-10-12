from random import choice
import matplotlib.pyplot as plt
import json

class RandomWalk:
    def __init__(self, step_count=5000, starting_x=0, starting_y=0, x_max_speed=4, y_max_speed=4):
        self.step_count = step_count
        self.x_coord = [starting_x]
        self.y_coord = [starting_y]
        self.x_max_speed = x_max_speed
        self.y_max_speed = y_max_speed

    def get_step(self, max_speed):
        direction = choice([1, -1])
        speed = choice(range(max_speed + 1))
        distance = direction * speed

        return distance


    def walk(self):
        while len(self.x_coord) <= self.step_count:
            x_distance = self.get_step(self.x_max_speed)
            y_distance = self.get_step(self.y_max_speed)

            if x_distance == 0 and y_distance == 0:
                continue

            x_new_coord = self.x_coord[-1] + x_distance
            y_new_coord = self.y_coord[-1] + y_distance
            self.x_coord.append(x_new_coord)
            self.y_coord.append(y_new_coord)

while True:
    step_count_input = input("How many steps would you like to walk (type 'q' to quit)? ")
    if step_count_input.lower() == 'q':
        break

    try:
        step_count = int(step_count_input)
    except ValueError:
        print("You did not enter a positive integer step count.")
        continue
    else:
        with open("cmap_text.txt", "r") as file_content:
            cmap_text = file_content.read()
        with open("cmap_list.json", "r") as file_content:
            cmap_list = json.load(file_content)

        cmap = input("What is your colormap style for the random walk (select from the styles below):\n"
                     + "---\n"
                     + cmap_text
                     + "---\n"
                     + "Colormap style: ")
        while cmap not in cmap_list:
            print("You did not enter a colormap style that is available.")
            cmap = input("Please enter a new colormap style: ")

        rw = RandomWalk(step_count)
        rw.walk()
        if cmap:
            print(cmap)
            plt.set_cmap(cmap)

        plt.scatter(0, 0, c='green', s=100)
        plt.scatter(rw.x_coord[-1], rw.y_coord[-1], c='red', s=100)
        plt.scatter(rw.x_coord, rw.y_coord, s=10, c=range(len(rw.x_coord)))
        plt.show()


