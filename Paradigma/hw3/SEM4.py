# # if __name__ == '__main__':
# # def normalize(data: list) -> list:
# #     x_max = max(data)
# #     x_min = min(data)
# #     return list(map(lambda x: (x - x_min) / (x_max - x_min), data))
# #
# # data1 = [1, 3, 5, 5, 1]
# # norm = normalize(data1)
# # print(data1)
# # print (norm)
# # 0, 0.5, 1, 1 ,0
#
# def get_count(data,age_filter):
#     count = 0
#     for age in data.values():
#         if age > age_filter:
#             count += 1
#     return count
#
#
# data = {"Pavel": 20, "Maxim": 42, "Sergey": 75, "Andrey": 18, "gena": 31}
# print(get_count(data, 30))

from random import randint

data_ = [randint(1, 5) for _ in range(10)]


def get_count(array):
    result = {}
    for i in data_:
        result[i] = result.get(i, 0) + 1
    return result


def dublicate(data_):
    unic = set(data_)
    counts = get_count(data_)
    return list(filter(lambda element: counts[element] > 1, unic))

print(data_)
print(dublicate(data_))

lst = list (range (1, 6))
print (lst)

tmp = map(lambda x: x * x, lst)
print(tmp)


def my_map(func, array):
    for item in array:
        yield func(item)


def my_filter(func, array):
    for item in array:
        if func(item):
            yield item


def frange(begin, end, step):
    while begin < end:
        yield begin
        begin += step


a = frange(1, 2, 0.3)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))

