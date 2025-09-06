import random as rnd

class Die:
    """A simple attempt to model a die."""

    def __init__(self, sides=6):
        """
        Set the attributes of a die.
        :param sides: the number of sides of the die.
        """
        self.sides= sides


    def roll_die(self) -> int:
        """Return a number after rolling the die."""
        return rnd.randint(1, self.sides)


def main():
    """Exercise 9-13 of the textbook."""
    # Make a 6-sided die and roll it 10 times.
    die1 = Die()
    for i in range(10):
        print(die1.roll_die())
    print()

    # Make a 10-sided die and roll it 10 times.
    die2 = Die(10)
    for i in range(10):
        print(die2.roll_die())
    print()

    # Make a 20-sided die and roll it 10 times.
    die3 = Die(20)
    for i in range(10):
        print(die3.roll_die())


# Call the main function.
if __name__ == '__main__':
    main()