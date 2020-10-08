def check_function(count_of_slice_first_list, index, list1, list2):
    """Функция проверки"""
    if list1[count_of_slice_first_list - 1][index:index + len(list2[0])] != list2[0]:
        return False
    check = 1
    list_1 = list1[count_of_slice_first_list:]  # удаление ненужных элементов первго списка
    list_2 = list2[1:]  # сдвиг 2го списка на 1 элемент т.к. мы его проверили
    for i in range(0, len(list_2)):
        slice_list1 = list_1[i][index:index + len(list2[0])]
        if slice_list1 == list_2[i]:
            check += 1
    if check == len(list2):
        return True
    else:
        return False


def TankRush(h1=int, w1=int, s1=str, h2=int, w2=int, s2=str):
    """Двумерное вхождение одного списка строк в другой"""
    if w1 < w2:  # неверный ввод данных (2ой список больше первого)
        return False
    if h1 < h2:  # неверный ввод данных (2ой список больше первого)
        return False
    list1 = s1.split(' ')  # координата подается строкой, разбиваем ее на список, разделитель - пробел
    list2 = s2.split(' ')
    count_of_index = 0
    for cord in list1:
        count_of_index += 1  # срез 1го списка
        if len(list1) - count_of_index < len(list2) - 1:  # проверка вхождения 2го списка в 1ый список по длине
            return False
        if list2[0] in cord:  # проверка вхождения 1го элемента 2го списка в текущий элемент 1го списка
            for i in range(0, w1):  # перебор всех подстрок единичной длинным на соответствие с 1ым элементом 2го списка
                if cord[i] == list2[0][0]:
                    result = check_function(count_of_index, i,  list1, list2)
                    if result is True:
                        return True
    if result is False:
        return False

