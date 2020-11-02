def string_splinter(data, strings, length, count):
    """Представление "колец" матрицы в ввиде прямоугольника и разворот прямоугольника (верхнее основание, правая
     сторона, нижнее основание(инфвертированное), левая сторона(инфвертированная) - порядок разворота) в прямую."""
    sub_string = ''
    if (count - 1) * 2 == 2 and strings < length:  # Прямоугольник со стороной равной 2 ( 2 строки).
        string = data[count - 1][count - 1: length - count + 1]
        string += data[count][length - count:count - 2:-1]
        return string
    elif (count - 1) * 2 == 2 and strings >= length:  # Прямоугольник со стороной равной 2 (Строк 2 и более).
        # Возвращает массив целых чисел!(*)
        array = []
        for i in range(count - 1, strings - count + 1):
            sub_string = data[i][count - 1:count + 1]
            array.append(sub_string)
        return array
    # Развертывание "колец" матрицы, суть выполнения команд описана в заголовке функции
    string = data[count - 1][0:]
    for i in range(count, strings - count):
        sub_string += data[i][length - count]
    string += sub_string
    sub_string = ''
    string += data[strings - count][::-1]
    for i in range(count, strings - count):
        sub_string += data[i][count - 1]
    string += sub_string[::-1]
    return string


def convert_last_string(data):
    """Конвертация массива с числами в массив со строками, случай когда в матрице 2 и более строк и 2 столбца."""
    result = []
    for i in range(0, len(data)):
        current_sub_string = ''
        for k in range(0, len(data[i])):
            current_sub_string += str(data[i][k])
        result.append(current_sub_string)
    return result


def step_right(string):
    """Смещение элементов вправо либо в строке, либо в списке."""
    if isinstance(string, str) is True:
        string = string[-1] + string[0:-1]
        return string
    else:
        data_n = []
        for i in range(0, len(string)):
            sub = []
            for k in range(0, len(string[i])):
                item = int(string[i][k])
                sub.append(item)
            data_n.append(sub)
        t = data_n[0][0]
        for i in range(0, len(string) - 1):
            data_n[i][0], data_n[i][1], t = data_n[i + 1][0], t, data_n[i][1]
        data_n[-1][0], data_n[-1][1] = data_n[-1][1], t
        data_n = convert_last_string(data_n)
        return data_n


def fill_new_data(data, strings, length, count, result):
    """Заполнение исходной матрицы, матрицей со сдвигом(заполнение идет кольцами), порядок - верхнее основание,
    правая сторона, нижнее основание(инвертированное), левая сторона(инвертированная). За исключениемпоследнего
    действия(if - elif) и первого(count == 1)."""
    if (count - 1) * 2 == 2 and strings < length:
        data[count - 1] = data[count - 1][0:count - 1] + result[0:length//2 + 1] + data[count - 1][length - count + 1:]
        result = result[len(result) // 2:]
        result = result[::-1]
        data[count] = data[count][0:count - 1] + result + data[count][length - count + 1:]
        return data
    elif (count - 1) * 2 == 2 and strings >= length:
        check = 0
        for i in range(count - 1, strings - count + 1):
            data[i] = data[i][0:count - 1] + result[check] + data[i][length - count + 1:]
            check += 1
        return data
    if count == 1:
        data[count - 1] = result[count - 1:length - count + 1]
    else:
        data[count - 1] = data[count - 1][0:count] + result[count - 1:length - count + 1] + data[count - 1][
                                                                                            length - count + 1:]
    result = result[length - count + 1:]
    if strings - count * 2 > 1:
        for i in range(count, strings - count):
            data[i] = data[i][0:length - count] + result[0]
            result = result[1:]
    bottom_string = result[count - 1: length - count + 1]
    bottom_string = bottom_string[::-1]
    if count == 1:
        data[strings - count] = bottom_string
    else:
        num = strings - count
        data[count - 1] = data[num][0:count] + bottom_string + data[num][length - count + 1:]
    result = result[length - count + 1:]
    result = result[::-1]
    if strings - count * 2 > 1:
        for i in range(count, strings - count):
            data[i] = result[0] + data[i][count:]
            result = result[1:]
    return data


def MatrixTurn(matrix, strings, length, step):
    """идея решения - рассмотреть смещение матрицы, как смещение ее "колец", кажое кольцо разворачиваем в прямую и
    сдвигаем вправо на одну цифру при каждом шаге."""
    if strings < length:
        moves_circles = strings // 2
    else:
        moves_circles = length // 2
    for steps_of_matrix in range(0, step):
        for steps in range(1, moves_circles + 1):
            circle = string_splinter(matrix, strings, length, steps)
            circle = step_right(circle)
            matrix = fill_new_data(matrix, strings, length, steps, circle)
    return matrix
