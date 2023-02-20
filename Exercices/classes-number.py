class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


# store the object Point() in variable point1
point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.move()

# new variable with the same attributes of the class, but different from first point1
point2 = Point()
point2.x = 30
print(point2.x)

numbers = [1, 2, 3]
