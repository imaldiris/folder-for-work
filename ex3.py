def ConquestCampaign(N, M, L, battalion):
    count_of_days = 1
    global_list = []
    cord_list = cords_for_steps(battalion)
    global_list = general_list(global_list, cord_list)
    while N * M != len(global_list):
        steps = step(N, M, cord_list)
        cord_list = steps[:]
        global_list = general_list(global_list, cord_list)
        count_of_days += 1
    return count_of_days


def cords_for_steps(battalion=list):
    new = []
    for i in range(0, len(battalion), 2):
        new.append([battalion[i], battalion[i + 1]])
    return new


def general_list(glob_list, k):
    for i in k:
        if i not in glob_list:
            current_cord = i
            glob_list.append(current_cord)
    return glob_list


def step(N, M, list_of_cords):
    new_list = []
    for i in list_of_cords:
        if i[0] < N:
            step_up = [i[0] + 1, i[1]]
            if step_up not in new_list:
                new_list.append(step_up)
        if i[0] > 1:
            step_down = [i[0] - 1, i[1]]
            if step_down not in new_list:
                new_list.append(step_down)
        if i[1] < M:
            step_right = [i[0], i[1] + 1]
            if step_right not in new_list:
                new_list.append(step_right)
        if i[1] > 1:
            step_left = [i[0], i[1] - 1]
            if step_left not in new_list:
                new_list.append(step_left)
    return new_list

