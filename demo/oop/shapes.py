from abc import abstractmethod, ABC


# abstract class 
class Point(ABC):
    def __init__(self, x, y):
        if x < 0 or y < 0:
            raise ValueError("Invalid Co-ordinates")
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x},{self.y}"

    @abstractmethod
    def area(self):
        pass


class Circle(Point):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def __str__(self):
        return f"{super().__str__()},{self.radius}"

    def area(self):
        return 0


class Rectangle(Point):
    def __init__(self, x, y, length, width):
        super().__init__(x, y)
        self.width = width
        self.length = length

    def __str__(self):
        return f"{super().__str__()},{self.length},{self.width}"

    def area(self):
        return 0


c = Circle(10, 20, 30)
print(c)
r = Rectangle(5, 5, 10, 20)
print(r)

print(issubclass(Circle, Point))
print(issubclass(Circle, Rectangle))
