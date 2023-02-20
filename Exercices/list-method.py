numbers = [5, 2, 1, 9, 10, 10]
# insert at the end of the list
numbers.append(20)
# insert number 35, second place in the list
numbers.insert(1, 35)
#numbers.clear()
# -- delete last one numbers.pop()
# print the number with the value 5
print(numbers.index(5))
#print(numbers)
print(numbers.count(2))
numbers.sort()
print(numbers)

number_copy = numbers.copy()
print('Numbers_copy: ', number_copy)

ze = numbers.count(10)
print('ze: ', ze)
