# Functions from previous solutions.

# Test if 'factor' is indeed a factor of 'value'
def is_factor(value, factor):
    return value % factor == 0

# Return the list of prime factors of 'value'
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

# Test if the list of prime facotrs if for a prime number
def is_list_prime(factor_list):
    if len(factor_list) == 0:
        return True
    else:
        return False
# Test if 'value' is a prime number
def is_prime(value):
	return is_list_prime(get_factors(value))      

# Return a list all prime numbers under 'value'
def get_primes(value):
	primes = []
	for i in range (2, value + 1):
		if is_prime(i):
			primes.append(i)
	return primes

# Return the nth prime, where 2 is the first
def get_nth_prime(n):
	primes = []
	value = 2
	while len(primes) < n:
		if is_prime(value):
			primes.append(value)
		value += 1
	return primes[n - 1]
