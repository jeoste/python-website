class Mammal:
    def __init__(self, name):
        # definition of the constructor
        self.name = name

    def walk(self):
        print(self.name + ' is walking')


class Dog(Mammal):
    pass


class Cat(Mammal):
    def meow(self):
        print(self.name + " is meowing")


class Human(Mammal):
    pass


human = Human(name="John")
print('Name: ', human.name)
human.walk()

dog = Dog(name="Woof")
print('Name: ', dog.name)
dog.walk()

cat = Cat(name="Rupi")
print('Name: ', cat.name)
cat.walk()
cat.meow()
