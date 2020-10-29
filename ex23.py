def changer_data(data):
    """Принимает список строку формата '..+.', где '.' - место для ветки, '+' - ветка и возвращает список списков
     в формате [0,0,1,0] и наоборот"""
    result = []
    for item in data:
        if isinstance(data[0], str) is True:
            sub_result = []
            for symbol in item:
                if symbol == '.':
                    sub_result.append(0)
                else:
                    sub_result.append(1)
            result.append(sub_result)
        else:
            sub_result = ''
            for symbol in item:
                if symbol != 0:
                    sub_result += '+'
                else:
                    sub_result += '.'
            result.append(sub_result)
    return result


def growth(data):
    """Рост веток, увеличение жизни на 1."""
    for item in data:
        for i in range(0, len(item)):
            item[i] += 1
    return data


def cord_of_branch_for_death(data):
    """Записывает кординаты веток возраст которых >= 3"""
    cord_list = []
    for line in range(0, len(data)):
        for pillar in range(0, len(data[line])):
            if data[line][pillar] >= 3:
                cord_list.append([line, pillar])
    return cord_list


def death_of_branches(list_of_death, data):
    """Определяет какие ветки умрут, с возрастом 3 и более."""
    cord_of_all_death_branches = []
    if len(list_of_death) == 0:
        return data
    for cord in list_of_death:
        cord_of_all_death_branches.append(cord)  # Определение колличества веток необходимых для удаления по вертикали
        # и горизонтали
        if cord[0] - 1 >= 0:
            cord_of_all_death_branches.append([cord[0] - 1, cord[1]])  # вертикаль
        if len(data) - (cord[0] + 1) > 0:
            cord_of_all_death_branches.append([cord[0] + 1, cord[1]])  # вертикаль
        if cord[1] - 1 >= 0:
            cord_of_all_death_branches.append([cord[0], cord[1] - 1])  # горизонталь
        if len(data[0]) - (cord[1] + 1) > 0:
            cord_of_all_death_branches.append([cord[0], cord[1] + 1])  # горизонталь
    for i in cord_of_all_death_branches:
        data[i[0]][i[1]] = 0
    return data


def TreeOfLife(h, w, n, tree):
    """Основная функция"""
    tree = changer_data(tree)
    for day in range(0, n):
        tree = growth(tree)
        if day % 2 == 1:
            death_list = cord_of_branch_for_death(tree)
            tree = death_of_branches(death_list, tree)
    tree = changer_data(tree)
    return tree

