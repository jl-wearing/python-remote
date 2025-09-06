# Program to calculate average test scores for each student.

def get_number_of_students() -> int:
    """Get the number of students to calculate averages for."""
    number_of_students = int(input('How many students do you have?: '))

    # Validate the number of students.
    while number_of_students < 0:
        print('ERROR: number of students cannot be negative.')
        number_of_students = int(input('How many students do you have?: '))

    return number_of_students


def get_number_of_scores() -> int:
    """Get the number of scores to calculate averages for."""
    number_of_scores = int(input('How many scores does each student have?: '))

    # Validate the number of scores.
    while number_of_scores < 0:
        print('Error: number of scores cannot be negative.')
        number_of_scores = int(input('How many scores does each student have?: '))

    return number_of_scores


def calculate_average(number_of_students: int, number_of_scores: int):
    """Calculate the average of each student."""
    for student in range(1, number_of_students+1):
        total = 0.0
        print(f'Student number {student}')
        print('-' * 20)
        for test in range(1, number_of_scores+1):
            # Input each score.
            test_score = float(input(f'Test number {test}: '))
            total += test_score
        print()

        # Calculate the average.
        average = total / number_of_scores

        # Output the average.
        print(f"Average for student {student}: {average:.2f}\n")


def main():
    """Mainline logic for calculating the average of each student."""
    # Get the number of students.
    number_of_students = get_number_of_students()

    # Get the number of scores of each student.
    number_of_scores = get_number_of_scores()

    # Calculate and display the average for each student.
    calculate_average(number_of_students, number_of_scores)


# Call the main function.
if __name__ == '__main__':
    main()