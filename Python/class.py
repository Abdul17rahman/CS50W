#Classes are templates of an object and are created as shown below.

#Create a class point
class Point():
    #This init function is a constructor function that calls the class its self
    def __init__(self, x, y):
        self.x = x
        self.y = y

#Using a class by creating an object
p = Point(12,4)

print(p.x)
print(p.y)