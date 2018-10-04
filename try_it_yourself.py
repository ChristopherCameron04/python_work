numbers = list(range(1,1000001))
print(max(numbers))
print(min(numbers))
print(sum(numbers))


odd_numbers= list(range(1,21,2))
for number in odd_numbers:
	print(number)


threes = list(range(3,31,3))
for number in threes:
	print(number)

cubes = [number**3 for number in range(1,10)]
print(cubes)
