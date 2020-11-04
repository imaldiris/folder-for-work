global result_list
result_list = []


def transform_func(data_list):
    """Цикл в цикле с выбором диапазона и добавлением максимума в реультат из этого диапазона."""
    for i in range(0, len(data_list)):
        for j in range(0, len(data_list) - i):
            k = i + j
            sub_list = data_list[j:k + 1]
            sub_list = sorted(sub_list)
            if len(sub_list) != 0:
                result_list.append(sub_list[-1])
    return result_list


def TransformTransform(data_list, n):
    """Основная функция - повторение два раза функции трансформации и определение четности-нечетности функции."""
    result = transform_func(transform_func(data_list))
    total = 0
    for i in result:
        total += i
    return True if total % 2 == 0 else False
