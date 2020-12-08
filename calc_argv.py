import sys

# FUNCTIONS
def division(a, b):
	a = int(a)
	b = int(b)
	c = a / b
	print(f"\n Result: {c}")

def multiply(a, b):
	a = int(a)
	b = int(b)
	c = a a b
	print(f"\n Result: {c}")

def addition(a, b):
	a = int(a)
	b = int(b)
	c = a + b
	int(c)
	print(f"\n Result: {c}")

def substraction(a, b):
	a = int(a)
	b = int(b)
	c = a - b
	print(f"\n Result: {c}")

# USE FUNCTION DEPEND ON ARGV
if sys.argv[1] == "d":
	division(sys.argv[2], sys.argv[3])
elif sys.argv[1] == "m":
	multiply(sys.argv[2], sys.argv[3])
elif sys.argv[1] == "a":
	addition(sys.argv[2], sys.argv[3])
elif sys.argv[1] == "s":
	substraction(sys.argv[2], sys.argv[3])

