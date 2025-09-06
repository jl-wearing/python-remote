import random

def get_lottery_values() -> list:
    """Return a list containing 10 numbers and 5 letters."""
    letters = random.choices(list("abcdefghijklmnopqrstuvwxyz"), k=5)
    numbers = list("0123456789")
    combined = letters + numbers
    return combined


def pick_lottery_values(combined_list: list) -> list:
    """Randomly pick 4 values from the combined list."""
    return sorted(random.choices(combined_list, k=4))


def display_correct_lottery_ticket(correct_lottery_ticket: list) -> None:
    """Display the correct lottery ticket."""
    print("Any ticket matching these 4 values wins a prize: ")
    for value in correct_lottery_ticket:
        print(value, end=' ')
    print()