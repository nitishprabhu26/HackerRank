if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i**2)


# The range() function

# The range function is a built in function that returns a series of numbers. At a minimum, it needs one integer parameter.

# Given one parameter, n, it returns integer values from 0 to n-1. For example, range(5) returns the numbers 0 through 4 in sequence.
# To start at a value other than 0, call range with two arguments. For example, range(1,5) returns the numbers 1 through 4.
# Finally, you can add an increment value as the third argument. For example, range(5, -1, -1) produces the descending sequence from 5 through 0 and range(0, 5, 2) produces 0, 2, 4. If you are going to provide a step value, you must also include a start value.