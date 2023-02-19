price = 1000000
hasGoodCredit = str(input('Do you have good credit? (Y) or (N) '))

if hasGoodCredit == 'Y' or hasGoodCredit == 'y':
    ten_percent = price * (10 / 100)
    print('You have to pay $', ten_percent, ' of the price')
    print('Total is: $', price - ten_percent)
elif hasGoodCredit == 'N' or hasGoodCredit == 'n':
    twenty_percent = price * (20 / 100)
    print('You have to pay $', twenty_percent, ' of the price')
    print('Total is: $', price - twenty_percent)
else:
    print('Verify your input.')
