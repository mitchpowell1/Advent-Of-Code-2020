input_numbers = set([int(line) for line in open('input.txt', 'r')])

for number in input_numbers:
	adder = 2020 - number
	if adder in input_numbers:
		print('Number 1: {}'.format(number))
		print('Number 2: {}'.format(adder))
		print('Sum: {}'.format(number + adder))
		print('Product: {}'.format(number * adder))
		break
