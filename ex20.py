list_of_appendix = []
list_of_deletion = []
step_memory = []
result = ''
undo_key = False
undo_list = []


def check_input(input_string):
    """Проверка корректности введения команды"""
    commands = [1, 2, 3, 4, 5]
    com = int(input_string[0])
    data = input_string[2:]
    if com not in commands:
        return False
    if (com == 1 or com == 2) and (' ' not in input_string):
        return False
    if (com == 4 or com == 5) and (len(input_string) != 1):
        return False
    if com == 2:
        try:
            int(data)
        except ValueError:
            return False
    if com == 3:
        if ' ' not in input_string:
            return ''
        try:
            int(data)
        except ValueError:
            return ''
    return True


def add_to_lists(key_of_undo, current_list, data, steps, number_of_command):
    """Обновление памяти операций и обновление ее при выполненной undo - операция 4"""
    global result, undo_list
    if key_of_undo is True:
        if number_of_command == 1:
            current_list = [len(data)]
        else:
            current_list = [data]
        undo_list = []
        key_of_undo = False
        steps = [number_of_command]
    else:
        if number_of_command == 1:
            current_list.append(len(data))
        else:
            current_list.append(data)
        steps.append(number_of_command)
    return [current_list, key_of_undo, steps]


def addition(res, data):
    """Добавление строки к строке, операция 1"""
    res += data
    return res


def deletion(res, rem):
    """Удаление подстроки, если подстрока больше строки, удаляет всю строку, операция 2"""
    if len(rem) >= len(res):
        res = ''
        return res
    res = res[0:-1 * len(rem)]
    return res


def undo():
    """Отмена последней операции 1 или 2, если после undo выполняет 1 или 2, преидущие действия становится невозмжно
    отменить, операция 4"""
    global list_of_appendix, list_of_deletion, result, step_memory, undo_list, undo_key
    undo_key = True
    if step_memory[-1] == 1:
        string_for_undo = result[len(result) - list_of_appendix[-1]:]
        result = deletion(result, string_for_undo)
        del list_of_appendix[-1]
    else:
        string_for_undo = list_of_deletion[-1]
        result = addition(result, string_for_undo)
        del list_of_deletion[-1]
    undo_list.append(string_for_undo)
    undo_list.append(step_memory[-1])
    del step_memory[-1]
    return result


def redo():
    """ Откат undo, выполнение операции 1 или 2 без очистки списка памяти шагов, а наоброт дополняет его выполненной
    оперцией, операция 1 или 2"""
    global result, undo_list, step_memory, list_of_appendix, list_of_deletion
    if len(undo_list) == 0:
        return result
    if undo_list[-1] == 1:
        result = addition(result, undo_list[-2])
        list_of_appendix.append(len(undo_list[-2]))
    else:
        result = deletion(result, undo_list[-2])
        list_of_deletion.append(undo_list[-2])
    step_memory.append(undo_list[-1])
    undo_list = undo_list[0:-2]
    return result


def BastShoe(command):
    global list_of_deletion, undo_key, list_of_appendix, step_memory, result
    check = check_input(command)
    if check == False or check == '':
        return result
    com = int(command[0])
    data = command[2:]
    if com == 1:
        result = addition(result, data)
        changes = add_to_lists(undo_key, list_of_appendix, data, step_memory, com)
        list_of_appendix, undo_key, step_memory = changes[0], changes[1], changes[2]
        return result
    if com == 2:
        removed = result[len(result) - int(data):]
        result = deletion(result, removed)
        changes = add_to_lists(undo_key, list_of_deletion, removed, step_memory, com)
        list_of_deletion, undo_key, step_memory = changes[0], changes[1], changes[2]
        return result
    if com == 3:
        if int(data) > len(result) - 1:
            return ''
        else:
            call = result[int(data)]
            return call
    if com == 4:
        if len(step_memory) == 0:
            return result
        result = undo()
        return result
    if com == 5:
        result = redo()
        return result


a = BastShoe('1 привет')
print(a)
a = BastShoe('1 , Джон!')
print(a)
a = BastShoe('27')
print(a)
a = BastShoe('4')
print(a)
a = BastShoe('1  How are you?')
print(a)
a = BastShoe('4')
print(a)
a = BastShoe('4')
print(a)
a = BastShoe('4')
print(a)
a = BastShoe('50')
print(a)
a = BastShoe('5')
print(a)