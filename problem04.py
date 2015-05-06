# Find the largest palindrome made from the product of two 3-digit numbers.

import math

def is_palindrome(number):
    num_string = str(number)
    left = 0
    right = len(num_string) - 1
    while num_string[left] == num_string[right]:
        if left >= right:
            return True
        left += 1
        right -= 1
    return False    

def largest_palindrome(digits):
    minimun = int(-1 * (math.pow(10, digits - 1)))
    maximum = int(-1 * (math.pow(10, digits)))
    largest = 0
    print "minimun = %d maximum = %d" % (-1 * minimun, -1 * maximum)
    for i in range (minimun, maximum, -1):
        for j in range (minimun, maximum, -1):
            value = i * j
            palindrome = is_palindrome(value)
            if palindrome:
                if value > largest:
                    largest = value
    return largest

def main():
    print "%d is the larget palindrome." % (largest_palindrome(3))

if __name__  == "__main__":
    main()