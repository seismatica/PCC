from random import randint


class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        throw = randint(1, self.sides)
        return throw

    def throw_average(self, number_of_throws):
        throw_sum = 0
        print("---Throwing dice of " + str(self.sides) + " sides ---")
        for throw in range(number_of_throws):
            throw = randint(1, self.sides)
            print("You threw " + str(throw))
            throw_sum += throw

        average = throw_sum/number_of_throws
        print("\n---Summary---\n"
              + "You threw " + str(number_of_throws)
              + " times, with an average of " + '%.2f'%average)


die1 = Die(20)
die1.throw_average(10)