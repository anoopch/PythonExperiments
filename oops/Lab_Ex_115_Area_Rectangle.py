# Find Area of Rectangle using class concept
class Shape:
    def __init__(self, sides):
        self.sides = sides

    def area(self):
        print('Placeholder Parent method')


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.sides = 4
        super().__init__(self.sides)
        self.length = length
        self.breadth = breadth

    def area(self):
        """
        This function calculates the area of a rectangle with 4 sides. Length and breadth
        """
        super().area()
        return self.length * self.breadth


num01 = int(input('Enter the length of Rectangle - '))
num02 = int(input('Enter the Breadth of Rectangle - '))

my_object = Rectangle(num01, num02)
print(f'Rectangle has {my_object.sides}')
print('Area = ', my_object.area())
