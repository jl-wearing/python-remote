class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make: str, model: str, year: int) -> None:
        """
        Initialize the instance variables of a car.
        :param make: the make of the car.
        :param model: the model of the car.
        :param year: the year the car was manufactured.
        """
        self.make = make.lower()
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self) -> str:
        """Return a neatly formatted descriptive name."""
        return f"{self.make} {self.model} {self.year}".title()


    def read_odometer(self) -> None:
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")


    def update_odometer(self, mileage: float) -> None:
        """Set the odometer reading to the given value."""
        if mileage <= self.odometer_reading:
            return
        self.odometer_reading = mileage

    def increment_odometer(self, miles: float) -> None:
        """Add the given amount to the odometer reading."""
        if miles <= 0:
            return
        self.odometer_reading +=miles


    def fill_gas_tank(self) -> None:
        """Replenish the car's gas tank."""
        print(f"Adding gas to the tank!")


class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=40.0) -> None:
        """Initialize the battery's attributes."""
        self.battery_size = battery_size


    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")


    def get_range(self) -> float:
        """Print a statement about the range this battery provides."""
        return 2.0 * self.battery_size


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make: str, model: str, year: int, battery_size=None) -> None:
        """
        Initialize the instance variables of the parent class.
        Then initialize attributes specific to electric vehicles.
        """
        super().__init__(make, model, year)
        if battery_size:
            self.battery = Battery(battery_size)
        else:
            self.battery = Battery()


    # Showcasing inheritance.
    def fill_gas_tank(self) -> None:
        """Electric cars don't have gas tanks."""
        print("Electric cars don't have gas tanks.")


def main():
    """Main function."""
    # Create an instance of Car.
    my_first_car = Car("BMW", "X5", 2008)

    # Invoke the get_descriptive_name() on the instance.
    print(my_first_car.get_descriptive_name())

    # Invoke the read_odometer() method on the instance.
    my_first_car.read_odometer()

    # Update the odometer reading and read the new value.
    my_first_car.update_odometer(-10)
    my_first_car.read_odometer()
    print()
    my_first_car.update_odometer(100)
    my_first_car.read_odometer()

    # Increment the odometer reading.
    INCREMENT = 100
    my_first_car.increment_odometer(INCREMENT)
    my_first_car.read_odometer()


# Call the main function.
if __name__ == '__main__':
    main()