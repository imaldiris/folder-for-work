def SynchronizingTables(n, pay_list, id_list):
    global_list = []
    list_id = id_list[:]
    list_of_pay = pay_list[:]
    list_id.sort()
    list_of_pay.sort()
    for i in id_list:
        k = list_id.index(i)
        global_list.append(list_of_pay[k])
    return global_list

