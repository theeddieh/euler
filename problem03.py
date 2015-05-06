# What is the largest prime factor of the number 600851475143 ?

# Recursive?
# Start with 2, check if it is a prime factor
# Increment check value, check if it is prime, them check it again the main number
# If x % val == 0, divid val by facotr and start over, ad facot to list of 
# factors
import math

def is_factor(value, factor):
    return value % factor == 0

def factor(value):
    maximun_possible_factor = value // 2
    prime_factors = []
    for factor in xrange (2, maximun_possible_factor + 1):
        if value == 1:
            break
        while (is_factor(value, factor)):
            prime_factors.append(factor)
            value = value / factor
    return prime_factors

def is_prime(factor_list):
    if len(factor_list) == 0:
        return True
    else:
        return False

def max_factor(factor_list):
    max = 0
    for x in range (0, len(factor_list)):
        if max > factor_list[x]:
            max = factor_list[x]
    return max

def main():

    value = 600851475143
    print "factoring %d" % (value)
    factors = factor(value)
    print factors
    factors.sort()
    print "largest factor of %d is %d" % (value,factors.pop())

if __name__ == "__main__":
    main()