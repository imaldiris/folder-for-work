def TankRush(h1=int, w1=int, s1=str, h2=int, w2=int, s2=str):
    """Двумерное вхождение одного списка строк в другой"""
    if w1 < w2:
        return False
    if h1 < h2:
        return False
    list1 = s1.split(' ')  # координата подается строкой, разбиваем ее на список, разделитель - пробел
    list2 = s2.split(' ')
    cord_main_map = []  # список проверки одномерноего вхождения
    cord_list = []  # контрольный список, исключает повторения
    for cord in list1:
        for cord1 in list2:
            if cord1 not in cord_list and cord not in cord_main_map and cord1 in cord:
                cord_list.append(cord1)
                cord_main_map.append(cord)
                continue
    return True if len(cord_list) == len(list2) else False
