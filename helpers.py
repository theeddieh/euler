# Functions from previous solutions.

def is_factor(value, factor):
    return value % factor == 0

def get_factors(value):
    maximun_possible_factor = value // 2
    prime_factors = []
    for factor in xrange (2, maximun_possible_factor + 1):
        if value == 1:
            break
        while (is_factor(value, factor)):
            prime_factors.append(factor)
            value = value / factor
    return prime_factors

def is_list_prime(factor_list):
    if len(factor_list) == 0:
        return True
    else:
        return False

def is_prime(value):
	return is_list_prime(get_factors(value))      

def get_primes(value):
	primes = []
	for i in range (2, value + 1):
		if is_prime(i):
			primes.append(i)
	return primes
