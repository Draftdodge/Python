# 📌 Создайте класс прямоугольник.
# 📌 Класс должен принимать длину и ширину при создании экземпляра.
# 📌 У класса должно быть два метода, возвращающие периметр и площадь.
# 📌 Если при создании экземпляра передаётся только одна сторона,
# считаем что у нас квадрат.

class Rectangle:
    def __init__(self, length, width=None):
        self.length = length
        self.width = width if width else length

    def rect_len(self):
        return (self.length + self.width) * 2

    def rect_area(self):
        return (self.length * self.width)

d = Rectangle(4)
print(d.rect_area())
print(d.rect_len())

