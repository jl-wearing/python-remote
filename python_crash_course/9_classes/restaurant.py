from functools import total_ordering

@total_ordering
class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name: str, cuisine_type: str) -> None:
        """
        Set the instance variables of a restaurant.
        :param restaurant_name: the name of the restaurant.
        :param cuisine_type: the type of cuisine.
        """
        self.restaurant_name = restaurant_name.lower()
        self.cuisine_type = cuisine_type
        self.number_served = 0


    def describe_restaurant(self) -> None:
        """Describe the restaurant by name, cuisine type and number of customers served."""
        print(f"Restaurant name: {self.restaurant_name.title()}")
        print(f"Cuisine Type: {self.cuisine_type.title()}")
        print(f"Number of customers served: {self.number_served}")


    def open_restaurant(self) -> None:
        """Open the restaurant for orders."""
        print(f"{self.restaurant_name.title()} is open for business.")


    def __str__(self) -> str:
        """Return a string representation of this restaurant."""
        return f"Restaurant({self.restaurant_name}, {self.cuisine_type}) {self.number_served}"


    def __eq__(self, other: 'Restaurant') -> bool:
        """Return true if this restaurant's name and cuisine type is equal to the other's."""
        return self.restaurant_name == other.restaurant_name \
            and self.cuisine_type == other.cuisine_type


    def __lt__(self, other: 'Restaurant') -> bool:
        """Compare by first name, then by cuisine type if names are equal."""
        if self.restaurant_name == other.restaurant_name:
            return self.cuisine_type < other.cuisine_type
        return self.restaurant_name < other.restaurant_name


    def set_number_served(self, number_of_customers_served) -> None:
        """Sets the number of customers served."""
        if number_of_customers_served <=self.number_served:
            return
        self.number_served = number_of_customers_served


class IceCreamStand(Restaurant):
    """An ice cream stand is a specific kind of restaurant."""
    def __init__(self, restaurant_name: str, cuisine_type='ice cream') -> None:
        """
        Initialize the instance variables of a restaurant.
        Then initialize the attributes specific to ice cream stands.
        :param restaurant_name: the name of the restaurant.
        :param cuisine_type: the type of cuisine the restaurant sells.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'banana', 'caramel', 'strawberry']


    def display_flavors(self) -> None:
        """Display the flavors of ice cream stand."""
        print("The flavors offered by this ice cream stand are:")
        for flavor in self.flavors:
            print(f"\t{flavor}")


def main():
    """Mainline logic to test the Restaurant class."""
    # Make an instance of Restaurant.
    kfc = Restaurant("kfc", 'fast-food')

    # Print the 3 attributes individually.
    print(f"Restaurant name: {kfc.restaurant_name.title()}")
    print(f"Cuisine Type: {kfc.cuisine_type.title()}")
    print(f"Number of customers served: {kfc.number_served}")

    # Call both methods.
    kfc.describe_restaurant()
    kfc.open_restaurant()
    print()

    # modify the number of customers served.
    kfc.set_number_served(-10)
    print(kfc.number_served)
    kfc.set_number_served(200)
    print(kfc.number_served)

# Call the main function.
if __name__ == '__main__':
    main()