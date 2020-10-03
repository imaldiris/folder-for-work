def stop_time(glob_time, moment_red, moment_green):
    """время остановки на светофоре"""
    if glob_time % (moment_red + moment_green) < moment_red:
        stop_time = moment_red - glob_time % (moment_red + moment_green)
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
        global_time += stop_time(global_time, i[1], i[2])
        current_distance = i[0]
    global_time += l - track[-1][0]
    return global_time
