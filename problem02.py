# By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
# find the sum of the even-valued terms.

def fibonacci(n):
	if n < 2:
		return 1
	else:
		return fibonacci(n - 1) + fibonacci(n - 2)

def main():
	term = 0
	x = 0
	sum = 0
	while term < 4000000:
		term = fibonacci(x)
		if (term % 2 == 0):
			sum = sum + term
		print "x = %d fib = %d" % (x, term)
		x = x + 1
	print "sum = %d" % (sum)

if __name__ == "__main__":
	main()