# Создайте функцию генератор чисел Фибоначчи fibonacci.

def fibonacci():
    prev = 0
    yield prev
    next = 1
    yield next
    while True:
        res = prev+next
        prev = next
        next = res
        yield res


f = fibonacci()
for i in range(10):
     print(next(f))
