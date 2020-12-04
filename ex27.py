def input_check(f):
    list_for_check = f[:]
    list_for_check.sort()
    if f == list_for_check:
        return False


def check(f):
    list_for_check = f[:]
    list_for_check.sort()
    if f == list_for_check:
        return True
    else:
        return False


def first_and_last(f, n):
    cords = []
    for i in range(0, n - 1):
        if f[i] > f[i+1]:
            cords.append(i)
            break
    for i in range(n - 1, -1,-1):
        if f[i] < f[i-1]:
            if i not in cords:
                cords.append(i)
                break
    return cords


def first_method(f, cords):
    f_1 = f[:]
    f_1[cords[0]],f_1[cords[1]] = f_1[cords[1]],f_1[cords[0]]
    return f_1


def second_method(f, cords):
    slice_of_list = f[cords[0]:cords[1]+1]
    slice_of_list = slice_of_list[::-1]
    count = 0
    for i in range(cords[0], cords[1]+1):
        f[i] = slice_of_list[count]
        count += 1
    return f


def Football(f, n):
    """Main function"""
    result = input_check(f)
    if result == False:
        return result
    numbers = first_and_last(f, n)
    if len(numbers) == 1:
        return False
    result_1 = first_method(f, numbers)
    result_2 = second_method(f, numbers)
    result_1 = check(result_1)
    result_2 = check(result_2)
    if result_1 or result_2 is True:
        return True
    else:
        return False
