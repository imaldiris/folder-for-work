def digit_list(line):
    """Принимает строку и возвращает ее в цифровом виде списка с цифрами"""
    check_list = []
    count_star = 0
    count_point = 0
    for i in line:
        if i == "*":
            count_star += 1
            if count_point != 0:  # Обновление точек
                check_list.append(count_point)
            count_point = 0
        else:
            count_point += 1
            if count_star != 0:
                check_list.append(count_star)  # Обновление звездочек
            count_star = 0
    check_list.append(count_star)  # Обновление звездочек при последней итерации
    return check_list


def result_func(dig_list):
    """Обработка списка цифр на цикличность и исключение"""
    if len(dig_list) == 1:  # только звездочки
        return True
    for i in range(2, len(dig_list)):
        if dig_list[i] != dig_list[i - 2]:  # проверка на нераввенство чередующихся элементов
            return False
    return True


def LineAnalysis(line=str):
    if line[0] != '*' and line[-1] != '*':
        return False
    check_list = digit_list(line)
    result = result_func(check_list)
    return result
