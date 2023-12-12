import math

def pearson_correlation(arr_1, arr_2):
    # Проверка, что массивы одинаковой длины
    if len(arr_1) != len(arr_2):
        raise ValueError("Массивы имеют разную длинну")

    array_len = len(arr_1)

    # Расчет среднего значения
    arith_mean_x = sum(arr_1) / array_len
    arith_mean_y = sum(arr_2) / array_len

    variance_x = sum([(xi - arith_mean_x) ** 2 for xi in arr_1])
    variance_y = sum([(yi - arith_mean_y) ** 2 for yi in arr_2])

    covariance = sum([(xi - arith_mean_x) * (yi - arith_mean_y) for xi, yi in zip(arr_1, arr_2)])
    correlation = covariance / (math.sqrt(variance_x * variance_y))

    return correlation


array_1 = [43, 67, 1, 11, 32, 89, 21]
array_2 = [99, 17, 43, 25, 25, 19, 12]

correlation = round(pearson_correlation(array_1, array_2), 5)
print(f"Корреляция Пирсона: {correlation}")
