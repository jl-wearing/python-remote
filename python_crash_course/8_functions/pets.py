def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.\n")

def main():
    """Mainline logic to test the describe_pet function."""
    describe_pet('dog', 'kiwi')
    describe_pet('hamster', 'harry')

    # Testing with keyword arguments.
    describe_pet(animal_type='dog', pet_name='ziggy')
    describe_pet(pet_name='lila', animal_type='dog')

    # Testing the default argument.
    describe_pet('aron')

# Call the main function.
if __name__ == '__main__':
    main()