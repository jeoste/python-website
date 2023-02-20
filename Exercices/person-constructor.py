class Person:
    def __init__(self, name):
        # definition of the constructor
        self.name = name

    def talk(self):
        print("Hi I'm " + self.name + '!')


human = Person(name="John")
print('Name: ', human.name)
human.talk()
