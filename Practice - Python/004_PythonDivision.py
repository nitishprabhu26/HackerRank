if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)



# Tutorial:

# In Python, there are two kinds of division: integer division and float division.
# Integer Division:
# Integer division returns the floor of the division. That is, the values after the decimal point are discarded. It is written as '//' in Python 3. So, 1//3 = 0, 2//3 = 0 and 3//3 = 1. Integer values are precisely stored, so they are safe to use in comparisons.
# Float Division:
# Float division returns a floating point approximation of the result of a division. For example, . Only a certain number of values after the decimal can be stored, so it is not possible to store an exact binary representation of many floating point numbers. This sometimes leads to problems when comparing numbers or when rounding.