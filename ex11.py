def short_string(s1, s2):
    """Функция, принимает две строки и возвращает список [max,min]"""
    if s1 == s2:  # равенство двух строк
        return [s1, s2]
    if len(s1) < len(s2):  # проверка длин строк
        dif_len = len(s2) - len(s1)
        s1 = '0' * dif_len + s1
        return [s2, s1]
    elif len(s2) < len(s1):
        dif_len = len(s1) - len(s2)
        s2 = '0' * dif_len + s2
        return [s1, s2]
    else:  # проверка двух строк равной длины
        for i in range(0, len(s1)):
            if int(s1[i]) > int(s2[i]):
                return [s1, s2]
            elif int(s2[i]) > int(s1[i]):
                return [s2, s1]


def calculate(max=str, min=str):
    """Функция, выполняющая поразрядный счёт в обратном порядке, счёт в столбик перевернтуых чисел.
    Принимает две строки, возвразращает разность по модулю строкой"""
    result_string = ''
    key = True  # единица старшего разряда, при отрицательной разности меньшего разряда.
    for i in range(0, len(min)):
        result = 0
        if key is False:
            result -= 1
            key = True
        result += int(max[i]) - int(min[i])
        if result < 0:
            result += 10
            key = False
        result_string += str(result)
    return result_string[::-1]


def zero_deleter(string):
    """Функция, удаляющая незначащие нули."""
    if string[0] == '0':
        while string[0] == '0' and len(string) != 1:
            string = string[1:]
    return string


def changer(list=list):
    """Принимает список и переворачивает элементы(строки) и выдает список"""
    max = list[0][::-1]
    min = list[1][::-1]
    return [max, min]


def BigMinus(s1=str, s2=str):
    list_of_numbers = short_string(s1, s2)
    list_of_numbers = changer(list_of_numbers)
    result_string = calculate(list_of_numbers[0], list_of_numbers[1])
    result_string = zero_deleter(result_string)
    return result_string