temperature = int(input('What is the temperature outside? '))

if 30 <= temperature:
    print('HOT')
elif 20 <= temperature <= 29:
    print('WARM')
elif 10 <= temperature <= 19:
    print('FRESH')
elif 0 <= temperature <= 9:
    print('COLD')
else:
    print('Negative temperature')
