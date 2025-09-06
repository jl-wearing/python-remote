from car import ElectricCar

def main():
    """Testing inheritance of electric car class."""
    tesla = ElectricCar('tesla', 'model s', 2016, 240)
    print(tesla.get_descriptive_name())
    tesla.battery.describe_battery()
    range = tesla.battery.get_range()
    print(f"My battery's range is {range:.2f} miles.")

# Call the main function.
if __name__ == '__main__':
    main()