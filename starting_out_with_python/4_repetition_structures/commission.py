# Program to calculate sales commission for a number of people.

def get_input():
    """Get a salesperson's sales and commission rate."""
    sales = float(input('Enter the amount of sales: '))
    comm_rate = float(input('Enter the commission rate: '))
    return sales, comm_rate

def calculate_commission(sales: float, comm_rate: float) -> float:
    """Calculate the commission based on sales and commission rate."""
    return sales * comm_rate

def display_commission(commission: float) -> None:
    """Display the commission based on sales and commission rate."""
    print(f"The commission is ${commission:.2f}")

def main():
    """Mainline logic for calculating sales commissions."""
    keep_going = 'y'
    while keep_going == 'y':
        # Get the sales and commission rate for a salesperson.
        sales, comm_rate = get_input()

        # Calculate the commission for the salesperson.
        commission = calculate_commission(sales, comm_rate)

        # Display the commission.
        display_commission(commission)

        # Ask if you want to calculate for another salesperson.
        keep_going = input('Do you want to continue? (y/n): ')


# Call the main function.
if __name__ == '__main__':
    main()