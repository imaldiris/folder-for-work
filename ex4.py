def MadMax(n, tele=list):
    tele.sort()
    list_of_date = tele[:-1]
    global_list = list_of_date[0:n // 2] + [tele[-1]] + list_of_date[-1:n // 2 - 1:-1]
    return global_list

