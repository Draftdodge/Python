# Создайте вручную кортеж содержащий элементы разных типов.
# Получите из него словарь списков, где ключ - тип элемента,
# а значение - список элементов данного типа.

a = (1, 3.2, 'ede')
dict_ = {}
for i in a:
    dict_.setdefault(type(i),i)
   # dict_[type(i)].append(i)
print(dict_)