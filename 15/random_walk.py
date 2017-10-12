from random import choice
import matplotlib.pyplot as plt

class RandomWalk:
    def __init__(self, step_count=5000, starting_x=0, starting_y=0, x_max_speed=4, y_max_speed=4):
        self.step_count = step_count
        self.x_coord = [starting_x]
        self.y_coord = [starting_y]
        self.x_max_speed = x_max_speed
        self.y_max_speed = y_max_speed

    def walk(self):
        while len(self.x_coord) <= self.step_count:
            x_direction = choice([1, -1])
            x_speed = choice(range(self.x_max_speed+1))
            y_direction = choice([1, -1])
            y_speed = choice(range(self.y_max_speed+1))

            x_distance = x_direction * x_speed
            y_distance = y_direction * y_speed

            if x_distance == 0 and y_distance == 0:
                continue

            x_new_coord = self.x_coord[-1] + x_distance
            y_new_coord = self.y_coord[-1] + y_distance
            self.x_coord.append(x_new_coord)
            self.y_coord.append(y_new_coord)

while True:
    step_count_input = input("How many steps would you like to walk? ")
    if step_count_input.lower() == 'q':
        break

    try:
        step_count = int(step_count_input)
    except ValueError:
        print("You did not enter a positive integer step count.")
        continue
    else:
        rw = RandomWalk(step_count)
        rw.walk()
        plt.scatter(rw.x_coord, rw.y_coord, s=10, c=range(len(rw.y_coord)), cmap=plt.cm.hsv.blue)
        plt.show()



