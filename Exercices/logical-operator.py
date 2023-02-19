#
hasHighIncome = int(input('How much is your income per year? '))
hasGoodCredit = False

if 100_000 <= hasHighIncome:
    hasGoodCredit = True
    print('You can get a loan')
else:
    hasGoodCredit = False
    print('You cannot get a loan')

