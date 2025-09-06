# Program to return a dictionary of information about a person.

def build_person(first_name, last_name, middle_name='', age=None):
    """
    Return a dictionary of information about a person.
    :param first_name: The first name of the person.
    :param last_name: The last name of the person.
    :param middle_name: The middle name of the person, if any.
    :param age: The age of the person, if they wish to provide it.
    :return: A dictionary of information describing a person.
    """
    person = {'first': first_name.lower(), 'last': last_name.lower()}

    if middle_name:
        person['middle'] = middle_name.lower()
    if age:
        person['age'] = age

    return person

def main():
    """Mainline logic to test the build_person function."""
    person1 = build_person('justin', 'WEARING')
    person2 = build_person('jason', 'momoa', middle_name='aquaman')
    person3= build_person('clark', 'kent', age=100)

    # Output
    print(person1, person2, person3, sep='\n')

# Call the main function.
if __name__ =='__main__':
    main()