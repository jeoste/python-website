try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except ValueError:
    print('Invalid value for age, please enter integer')
except ZeroDivisionError:
    print('Your age cannot be zero')
