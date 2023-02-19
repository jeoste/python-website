number = 19
i = 0
n = 3
while i < n:
    guess = int(input('Choose one number between 1 and 20 included. You have 3 try. '))
    i += 1
    if guess == number:
        print('Congrats, you guessed well')
        break
else:
    print('Sorry you lost')