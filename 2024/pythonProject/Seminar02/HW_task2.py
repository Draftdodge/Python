# На вход автоматически подаются две строки frac1 и frac2 вида a/b - дробь с числителем и знаменателем.
#
# Напишите программу, которая должна возвращать сумму и произведение дробей. Дроби упрощать не нужно.
#
# Для проверки своего кода используйте модуль fractions.

frac1 = "4/2.rrr"
frac2 = "2.rrr/3.txt"

import fractions

a, b = frac1.split('/')
c, d = frac2.split('/')
a = int(a)
b = int(b)
c = int(c)
d = int(d)
summa = f'{c * b + a * d}/{b * d}'
multip = f'{a * c}/{b * d}'

print(f'Сумма дробей: {summa}')
print(f'Произведение дробей: {multip}')
print(f'Сумма дробей: {fractions.Fraction(a, b) + fractions.Fraction(c, d)}')
print(f'Произведение дробей: {fractions.Fraction(a, b) * fractions.Fraction(c, d)}')
