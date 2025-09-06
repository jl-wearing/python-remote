# Program to sort names entered by the user.

# Input
name1 = input('Enter a name (last name first): ')
name2 = input('Enter a name (last name first): ')

# Process
# Sort the names by ASCII score.
if name1 < name2:
    sorted_names = f"{name1.title()}\n{name2.title()}"
else:
    sorted_names= f"{name2.title()}\n{name1.title()}"

# Output
print("Here are the names, listed alphabetically:")
print(sorted_names)