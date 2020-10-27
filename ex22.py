def counter(string):
    """Принимает строку и считает плотность символов, выдает плотность без самих символов."""
    count_of_substring = []
    amount = 1
    for i in string:
        if i not in count_of_substring:
            count_of_substring.append(i)
            count_of_substring.append(amount)
        else:
            count_of_substring[count_of_substring.index(i) + 1] += 1
    count_of_substring = [count_of_substring[i] for i in range(1, len(count_of_substring) + 1, 2)]
    count_of_substring.sort()
    return count_of_substring


def check_validation(data):
    """Проверяет список(исходная строка см. функцию counter) на валидность"""
    most_included = most_included_symbols(data)
    count_of_dif = 0
    index = 0
    for i in data:
        if i != most_included:
            index = i
            count_of_dif += 1
    if count_of_dif > 1:
        return False
    if count_of_dif == 0:
        return True
    data = check_difference(data, index, most_included)
    return data


def most_included_symbols(data):
    """принимает список с плотностью элементов и выдает самый часто встречающийся"""
    current = data[0]
    count = 0
    max_amount = 0
    max_current = data[0]
    for i in data:
        if i == current:
            count += 1
        elif i != current:
            if count > max_amount:
                max_amount = count
                max_current = current
            count = 1
            current = i
    if count > max_amount:
        max_current = current
    return max_current


def check_difference(data, index_of_non_equal, len_of_most_included):
    """Принимает список плотности букв в слове и возвращает False или True при удалении одной буквы."""
    if data[data.index(index_of_non_equal)] == 1:
        return True
    if data[data.index(index_of_non_equal)] - 1 == len_of_most_included:
        return True
    else:
        return False


def SherlockValidString(string):
    """Основная функция"""
    list_of_amount = counter(string)
    data = check_validation(list_of_amount)
    if data is True:
        return True
    else:
        return False
