# Program to calculate the number of calories burned.

# Constants used by the program.
CALORIES_BURNED_PER_MINUTE = 4.2

def time_intervals() -> list[int]:
    """Get the time intervals you wish to display. """
    print("In what time intervals would you like your treadmill to display?", end=' ')
    print("press -1 to quit entering times: ")
    times= []
    while True:
        time = int(input())

        # Terminating condition.
        if time == -1:
            break

        times.append(time)

    times.sort()
    return times


def display_calories_burned(times: list[int]) -> None:
    """Display the number of calories burned after certain time intervals."""
    for time in times:
        print(f"Calories burned after {time} minutes: {CALORIES_BURNED_PER_MINUTE * int(time)}")


def main():
    """Main function for calculating calories burned on a treadmill."""
    # Get the times.
    times = time_intervals()

    # Display the calories burned.
    display_calories_burned(times)


# Call the main function.
if __name__ == '__main__':
    main()