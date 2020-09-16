def SynchronizingTables(n, id_list, pay_list):
    global_list = []
    list_id = id_list[:]
    list_of_pay = pay_list[:]
    list_id.sort()
    list_of_pay.sort()
    for i in id_list:
        k = list_id.index(i)
        global_list.append(list_of_pay[k])
    return global_list


a = SynchronizingTables(4,[10,67,68,28],[55,73,10,6])
print(a)