import sys

num = int(sys.argv[1])
steps = 1e3
s = 0

while s < steps:

	if num <= 1:
		exit()

	elif num%2 == 0:
		print(int(num/2))
		num = int(num/2)

	else:
		print(num*3+1)
		num = int(num*3+1)

	s = s+1