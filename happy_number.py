# Write an algorithm to determine if a number n is "happy".
#
# A happy number is a number defined by the following process: Starting with any positive integer,
# replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay),
# or it loops endlessly in a cycle which does not include 1.
#
# Those numbers for which this process ends in 1 are happy numbers.
#
# Return True if n is a happy number, and False if not.


def sumSquare(n):
    sum = 0
    while n > 0:
        d = n % 10
        sum += d * d
        n = n / 10
    return sum


def is_happy(n):
    if n == 1 or n == 7:
        return True

    marked = {}
    while True:
        sum = sumSquare(n)
        if sum == 1:
            return True

        if sum in marked:
            break
        else:
            marked[sum] = True
        n = sum

    return False


# using slow and fast pointer like checking cycled link-list
def is_happy_1(n):
    if n == 1 or n == 7:
        return True

    while True:
        slow = sumSquare(n)
        fast = sumSquare(sumSquare(n))

        if slow == 1:
            return True

        if slow == fast:
            return False

        n = slow

    return False

