import math


def new_string(s, encode):
    """Функция, удаляющая пробелы из входной строки и возвращающая строку без пробелов"""
    string = ''
    if encode == True:
        for i in s.lower():
            if i != ' ':
                string += i
        return string
    else:
        return s


def matrix(string):
    """Функция, определяющая размер строки матрицы"""
    sqr_root = math.sqrt(len(string))
    max_edge = math.trunc(sqr_root) + 1
    return max_edge


def encode(string, edge, encode):
    """Функция кодирующая матрицу и возвращающая строку"""
    result_string = ''
    global_list = []
    if encode == True:
        while len(string) != 0:  # заполнение матрицы при шифровке
            if len(string) >= edge:
                global_list.append([string[0:edge]])
                string = string[edge:]
            else:
                spaces = (edge - len(string)) * ' '  # пробелы в конце
                global_list.append([string[:] + spaces])
                string = ''
    else:
        list = string.split(' ')  # разбиение строки для расшифровки в список
        global_list = [[i] for i in list]
    for i in range(0, edge):  # вывод строки в нужном порядке(шифровка)
        for word in global_list:
            if word[0][i:i+1] != ' ':
                result_string += word[0][i:i+1].lower()
            if (word == ' ' or global_list.index(word) == len(global_list) - 1) and encode == True:
                result_string += ' '
    return result_string


def TheRabbitsFoot(string, bool):
    changed_string = new_string(string, bool)
    edge = matrix(changed_string)
    result_string = encode(changed_string, edge, bool)
    return result_string
