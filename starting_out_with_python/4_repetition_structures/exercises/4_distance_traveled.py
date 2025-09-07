# Program to calculate the distance a vehicle travelled for every hour under motion.

def get_speed() -> float:
    """Get the speed a vehicle travels."""
    speed = float(input('Enter the average speed of the vehicle: '))

    # Input validation.
    while speed < 0:
        speed = float(input('Speed cannot be negative. Enter average speed: '))

    return speed


def get_time() -> int:
    """Get the number of hours a vehicle travels."""
    time = int(input('Enter the number of hours a vehicle traveled: '))

    # Input validation
    while time < 0:
        time = int(input('Time cannot be negative. Enter number of hours a vehicle traveled: '))

    return time


def display_distance_per_hour(speed: float, time: int) -> None:
    """Display the distance traveled for every hour under motion."""
    print(f"\nHour\t\tDistance Traveled")
    for i in range(1, time+1):
        # Calculate the distance traveled.
        distance = speed * i

        # Display the distance for time i.
        print(f"{i}{distance:20.2f}")


def main() -> None:
    """Main function for calculating distance traveled for every hour under motion."""
    # Get the speed of the vehicle.
    speed = get_speed()

    # Get the number of hours the vehicle traveled.
    time = get_time()

    # Output
    display_distance_per_hour(speed, time)


# Call the main function.
if __name__ == '__main__':
    main()