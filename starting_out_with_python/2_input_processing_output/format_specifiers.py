# You can use format specifiers for rounding floating point numbers.
# .2f, .2 is the precision designator, f is the type designator

# You can use format specifiers to insert comma separators.
# {:,.2f}

# You can use the % symbol to convert a float to a percentage.
# % causes the float to be multiplied by 100 and displayed with a % sign.
# {:.2%}

# You can display numbers in scientific notation using e or E.
# {:.2e}

# You can specify a field width designator which is the minimum number of
# spaces required to show the value.
number = 99
print(f"The number is {number:10d}")
number= 12345.6789
print(f"The number is {number:12,.2f}")

# You can use format specifier to align values.
# By default, numbers are aligned to the right and strings are aligned to the left.
# You can change the default alignment using an alignment designator.
# < left align, > right align, ^ center align

# The order of designators: [alignment][width][,][.precision][type]