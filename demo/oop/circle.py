class Circle:
    # Static (class)  attributes
    max_radius = 100

    @staticmethod
    def set_max_radius(newmax):
        Circle.max_radius = newmax

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        if radius > Circle.max_radius:
            raise ValueError("Invalid Radius")

        self.radius = radius

    def __str__(self):
        return f"{self.x},{self.y} {self.radius}"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.radius == other.radius

    def __gt__(self, other):
        return self.radius > other.radius


circles = [Circle(10, 20, 10), Circle(5, 5, 25), Circle(30, 40, 5), Circle(10, 20, 30)]
for c in sorted(circles):
    print(c)
