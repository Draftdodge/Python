class Rectangle:
    def __init__(self, width, height=None):
        self.width = width
        if height == None:
            self.height = width
        else:
            self.height = height

    def perimeter(self):
        return (self.height + self.width) * 2

    def area(self):
        return (self.height * self.width)
    def __add__(self, other: 'Rectangle'):
        new_perimetr = self.perimeter() + other.perimeter()
        new_height = self.height + other.height
        new_width = self.width + other.width
        return Rectangle(new_width, new_height)
    def __sub__(self, other):
        new_perimetr = self.perimeter() - other.perimeter()
        new_height = self.height - other.height
        new_width = self.width - other.width
        return Rectangle(new_width, new_height)
    def __lt__(self, other):
        if self.area() < other.area():
            return True
        return False

    def __eq__(self, other):
        if self.area() == other.area():
            return True
        return False
    def __le__(self, other):
        if self.area() <= other.area():
            return True
        return False
    def __str__(self):
        return f"Прямоугольник со сторонами {self.width} и {self.height}"
    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"


rect1 = Rectangle(5, 10)
rect2 = Rectangle(3, 7)

print(f"Периметр rect1: {rect1.perimeter()}")
print(f"Площадь rect2: {rect2.area()}")
print(f"rect1 < rect2: {rect1 < rect2}")
print(f"rect1 == rect2: {rect1 == rect2}")
print(f"rect1 <= rect2: {rect1 <= rect2}")

rect3 = rect1 + rect2
print(f"Периметр rect3: {rect3.perimeter()}")
rect4 = rect1 - rect2
print(f"Ширина rect4: {rect4.width}")
