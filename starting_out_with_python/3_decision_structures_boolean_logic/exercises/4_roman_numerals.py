# Program to display roman numerals of the first 10 numbers.

# Input
number = int(input('Enter a number between 1 and 10: '))

# Process
match number:
    case 1:
        roman_numeral = 'I'
    case 2:
        roman_numeral = 'II'
    case 3:
        roman_numeral = 'III'
    case 4:
        roman_numeral = 'IV'
    case 5:
        roman_numeral = 'V'
    case 6:
        roman_numeral = 'VI'
    case 7:
        roman_numeral = 'VII'
    case 8:
        roman_numeral = 'VIII'
    case 9:
        roman_numeral = 'IX'
    case 10:
        roman_numeral = 'X'
    case _:
        roman_numeral = 'Invalid Input'

# Output
print(roman_numeral)