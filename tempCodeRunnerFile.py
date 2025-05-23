class circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

    def perimeter(self):
        return (22 / 7) * 2 * self.radius


c = circle(4)

print(c.area())
print(c.perimeter())