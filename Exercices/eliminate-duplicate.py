numbers = [1, 3, 3, 5, 10, 25, 25, 25, 30]

#duplicate = numbers[0]

number = 0
for number in numbers:
    if numbers.count(number) > 1:
        numbers.remove(number)
print('First method: ', numbers)

numbers_2 = [1, 3, 3, 5, 10, 25, 25, 16, 16, 4, 4, 30]
unique = []
for number_2 in numbers_2:
    if number_2 not in unique:
        unique.append(number_2)
print('Second method unique: ', unique)

