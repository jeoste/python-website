def hello_parameter(greet: str):
    print("Hello", greet)
    # return greet


hello_parameter("world")


# keyword argument. Whatever the position, because we specified the parameter with the variable
# it'll be used in the function in the right order
def greet_user(first_name):
    print('Hi', first_name)


def shopping_cost(discount, shipping, price) -> int:
    total_sum = (price * (discount / 100) + price) + shipping
    return total_sum


def calc_square(length) -> int:
    square_length = length * length
    return square_length


length = int(input('Enter length of square: '))
print("Length: ", length)
# function(parameter) to receive the result of return inside the function. Don't pass return in another variable
print("Square length: ", calc_square(length))


greet_user(first_name="Joe")

print('Cost is: $', shopping_cost(shipping=10, price=50, discount=5))

#print('Area of square: ', area)
