# Напишите функцию key_params, принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ - значение переданного аргумента, а значение - имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.

def HashableOrUnhashable(obj):
    try:
        hash(obj)
        return True
    except Exception as ex:
        return False
def key_params(**kvargs):
    '''Возвращает словарь, где ключ — значение переданного в функцию аргумента, а значение — имя аргумента'''

    result_dict = {}
    for values, key in kvargs.items():
        if HashableOrUnhashable(key):
            result_dict[key] = values
        else:
            result_dict[str(key)] = values
    return result_dict

params = key_params(a=1, b='hello', c=[1, 2, 3], d={})
print(params)
