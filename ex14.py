def stop_time(glob_time, moment):
    """время остановки на светофоре"""
    if (glob_time//moment) % 2 == 0:
        stop_time = moment * (glob_time//moment + 1) - glob_time
        return stop_time
    else:
        return 0


def Unmanned(l, n, track):
    current_distance = 0
    global_time = 0
    if l <= track[0][0]:
        return l
    for i in track:
        current_distance = i[0] - current_distance
        global_time += current_distance
        global_time += stop_time(global_time, i[1])
        current_distance = i[0]
    global_time += l - track[-1][0]
    return global_time

