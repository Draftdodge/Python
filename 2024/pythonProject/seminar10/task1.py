# 📌 Создайте класс окружность.
# 📌 Класс должен принимать радиус окружности при создании экземпляра.
# 📌 У класса должно быть два метода, возвращающие длину окружности и её площадь.

import math


class Circle:
    pi = math.pi #атрибут класса (Свойства класса)
    def __init__(self, radius):
        self.radius = radius #атрибут экземпляра

    def circle_length(self):
        return 2 * self.pi * self.radius

    def circle_area(self):
        return self.pi * self.radius ** 2


circle = Circle(4)
print(circle.circle_length())
print(circle.circle_area())
