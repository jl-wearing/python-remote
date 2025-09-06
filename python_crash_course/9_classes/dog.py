from functools import total_ordering

@total_ordering
class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name: str, age: int) -> None:
        """
        Initialize name and age instance variables.
        :param name: the name of the dog.
        :param age: the age of the dog.
        """
        self.name = name.lower()
        self.age = age

    def __str__(self):
        """Return a string representation of the dog."""
        return f'Dog({self.name}, {self.age})'

    def __eq__(self, other: 'Dog') -> bool:
        """Return true if this dog's name and age are equal to the other."""
        return (self.name, self.age) == (other.name, other.age)

    def __lt__(self, other: 'Dog') -> bool:
        """Return true if this dog's name and age are less than the other."""
        return (self.name, self.age) < (other.name, other.age)

    def sit(self) -> None:
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name.title()} is now sitting.")

    def roll_over(self) -> None:
        """Simulate a dog rolling over in response to a command."""
        print(f"{self.name.title()} rolled over.")

def main():
    """Mainline logic to test the Dog class."""
    my_dog = Dog('Kiwi', 7)

    # Output the dog's attributes.
    print(f"My dog's name is {my_dog.name.title()}.")
    print(f"My dog is {my_dog.age} years old.")

    # Testing the accessor methods of class Dog.
    my_dog.sit()
    my_dog.roll_over()
    print(my_dog)

    # Testing the equality methods.
    other_dog = Dog('Ziggy', 13)
    same_dog = Dog('Kiwi', 7)
    print(my_dog < other_dog)
    print(my_dog == same_dog)

# Call the main function.
if __name__ == '__main__':
    main()
