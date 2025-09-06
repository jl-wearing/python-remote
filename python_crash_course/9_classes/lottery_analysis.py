# Play the lottery game and determine the probability of getting the correct ticket.
import lottery

def main():
    """Playing the lottery game and determine how many tries it takes to win."""

    # Get the lottery values.
    lottery_values = lottery.get_lottery_values()

    # Set the values to retrieve from in this lottery.
    correct_ticket = lottery.pick_lottery_values(lottery_values)

    # Determine how many tries it takes to get the correct ticket.
    counter = 0
    while True:
        counter += 1

        # Draw a ticket.
        draw = sorted(lottery.pick_lottery_values(lottery_values))

        if draw == correct_ticket:
            break

    # Output
    print(f"It took {counter} tries to win.")


# Call the main function.
if __name__ == '__main__':
    main()