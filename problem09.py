# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import math

# Gross. Super brute force here. n^3, yikes
def calculate():
	for a in range (1, 1000):
		for b in range (1, 1000):
			for c in range (1, 1000):
				if (a + b + c == 1000):
					triples = [a, b, c]
					triples.sort()
					if (math.pow(triples[0], 2) + math.pow(triples[1], 2) == math.pow(triples[2], 2)):
						return a * b * c

def main():
	print calculate()

if __name__ == "__main__":
	main()