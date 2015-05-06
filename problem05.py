# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import helpers

def main():
	value = 20
	primes = helpers.get_primes(value)
	print primes	

	product = 1
	for i in primes:
		product *= i
	print product


if __name__ == "__main__":
	main()