import random

dice1 = [1, 2, 3, 4, 5, 6]
dice2 = [1, 2, 3, 4, 5, 6]

throw = random.choice(dice1)
throw2 = random.choice(dice2)
print('(', throw, ', ', throw2, ')')


class Dice:
    def roll(self):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        return dice1, dice2


dice = Dice()
print(dice.roll())
