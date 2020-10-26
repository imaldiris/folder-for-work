def id_function(data):
    """Принимает входную строку(1) или список id(2), возварщает список id(1) или выходную строку(2)"""
    if isinstance(data, str) is True:  # 1
        list_of_id = []
        for i in data:
            list_of_id.append(ord(i))
        return list_of_id
    if isinstance(data, list) is True:  # 2
        result = ''
        for i in data:
            result += chr(i)
        return result


def BiggerGreater(string):
    maximum_digit = 0
    k = id_function(string)
    for i in range(-1, -1 * len(k), -1):  # Определение разряда для замены
        count = i
        if k[i] > k[i - 1]:
            current_digit = k[i]
            maximum_digit = k[i - 1]
            break
    if maximum_digit == 0:  # Невозможно составить слово, элементы по убыванию или равны.
        return ''
    for i in range(-1, count - 2, - 1):  # Перестановка минимально большего разряда в найденный для замены
        if maximum_digit < k[i] <= current_digit:
            k[count - 1], k[i] = k[i], k[count - 1]
            current_digit = k[count - 1]
    sorted_part = k[count:]
    result = k[0:count] + sorted(sorted_part)
    result = id_function(result)
    return result
