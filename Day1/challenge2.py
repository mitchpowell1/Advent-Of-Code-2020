MAGIC_NUMBER = 2020

input_numbers = [int(line) for line in open('input.txt', 'r')]
input_numbers.sort()
input_set = set(input_numbers)

break_outer = False

for i in range(len(input_numbers) - 1):
	number1 = input_numbers[i]
	if break_outer:
		break

	for j in range(i + 1, len(input_numbers)):
		number2 = input_numbers[j]
		
		first_two_sum = number1 + number2

		if first_two_sum >= MAGIC_NUMBER:
			break

		needed_addend = MAGIC_NUMBER - first_two_sum

		if needed_addend in input_set:
			print('Number1: {}'.format(number1))
			print('Number2: {}'.format(number2))
			print('Number3: {}'.format(needed_addend))
			print('Sum: {}'.format(number1 + number2 + needed_addend))
			print('Product: {}'.format(number1 * number2 * needed_addend))
			break_outer = True
			break
