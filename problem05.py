# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

import math

def main():
	sum_squares = 0
	square_sums = 0

	for i in range (1, 101):
		sum_squares += math.pow(i, 2)
		square_sums += i
	square_sums = math.pow(square_sums, 2)
	diff = square_sums - sum_squares
	print int(diff)

if __name__ == "__main__":
	main()