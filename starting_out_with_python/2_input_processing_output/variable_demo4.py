# Program to showcase variable reassignment.

dollars = 2.75
print('I have', dollars, 'dollars.')

# reassignment
dollars = 99.95
print('But now I have', dollars, 'dollars.')

print(type(dollars))
if type(dollars) == float:
    print(True)
else:
    print(False)