from random import randint
import pygal


class Die:
    """Represent a single die"""
    def __init__(self, sides=6):
        """Store number of sides in the die"""
        self.sides = sides

    def roll(self):
        """Return random die value from one roll"""
        roll_value = randint(1, self.sides)
        return roll_value


def result_count(die_rolls, sides1, sides2, sides3):
    """
    :param die_rolls: list of die roll results
    :return: list of result occurrences from 0 to max die value
    """
    counts = [die_rolls.count(result) for result in range(3, sides1 + sides2 + sides3 + 1)]

    return counts


# # Create a die object
# die = Die()
#
# # Roll die 1000 times and store the results
# die_rolls = []
# for roll in range(1000):
#     die_rolls.append(die.roll())
# count = result_count(die_rolls, die.sides)
#
# # Display frequencies for each value using Pygal
# hist = pygal.Bar()
# hist.title = "Results of rolling one D6 1000 times"
# hist.x_labels = [str(n) for n in range(1, 7)]
# hist.x_title = "Result"
# hist.y_title = "Frequency of result"
#
# hist.add('D6', count)
# hist.render_to_file('die_visual.svg')


# Roll two dice and add up the frequencies
rolls = 500000
sides1 = 6
sides2 = 6
sides3 = 6
die1 = Die(sides1)
die2 = Die(sides2)
die3 = Die(sides3)
dice_rolls = [die1.roll() + die2.roll() + die3.roll() for roll in range(rolls)]
count2 = result_count(dice_rolls, sides1, sides2, sides3)

# Display frequency of rolling 2 dice
hist2 = pygal.Bar()
hist2.title = "Results of rolling one D" + str(sides1) + ", one D" + str(sides2) + ", and one D" + str(sides3) + \
              " " + str(rolls) + " times and adding results of each roll together"
hist2.x_labels = [str(n) for n in range(3, sides1 + sides2 + sides3 + 1)]
hist2.x_title = "Result"
hist2.y_title = "Frequency of result"

hist2.add('D' + str(sides1) + ' + D' + str(sides1), count2)
hist2.render_to_file('die_visual5.svg')
