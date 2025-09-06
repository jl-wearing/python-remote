# This program calculates sales commissions.

def main():
    while True:
        # Get a salesperson's sales and commission rate.
        sales = float(input('Enter the amount of sales: '))
        com_rate = float(input('Enter the commission rate: '))

        # Calculate the commission.
        commission = sales * com_rate

        # Display the commission.
        print(f"The commission is ${commission:,.2f}")

        # Keep going
        keep_going = input('Do you want to calculate the commission of another salesperson? (y/n): ').lower()
        if keep_going == 'n':
            break

# Call the main function
if __name__ == '__main__':
    main()