# def stop_time(glob_time, moment_red, moment_green):
#     """время остановки на светофоре"""
#     if glob_time % (moment_red + moment_green) < moment_red:
#         stop_time = moment_red - glob_time % (moment_red + moment_green)
#         return stop_time
#     else:
#         return 0
#
#
# def Unmanned(l, n, track):
#     current_distance = 0
#     global_time = 0
#     if l <= track[0][0]:
#         return l
#     for i in track:
#         current_distance = i[0] - current_distance
#         global_time += current_distance
#         global_time += stop_time(global_time, i[1], i[2])
#         current_distance = i[0]
#     global_time += l - track[-1][0]
#     return global_time

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