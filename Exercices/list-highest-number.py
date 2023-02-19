numbers = [1, 5, 100, 95, 77, 101]
print(numbers)

number = 0
# the max is the first element
highest = numbers[0]

for number in numbers:
    if number > highest:
        highest = number
        print('Highest number so far: ', highest)
print('Maximum number is: ', highest)
