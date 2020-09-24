def WordSearch(lenght, string, subs):
    word = ''
    current_list = []
    current_string = ''
    count = 0
    check = ''
    global_list = []
    for i in string:
        if i != ' ':
            if count == len(string) - 1:
                word = check + i
            else:
                count += 1
                check += i
                continue
        else:
            count += 1
            word = check[:]
            check = ''
        if len(current_string + word) <= lenght:
            current_string += word
            if len(current_string) < lenght:
                current_string += ' '
        else:
            if len(word) < lenght:
                current_list.append(current_string)
                global_list.append(current_list)
                current_list = []
                current_string = word[:] + ' ' if len(word) < lenght else word[:]
            if len(word) == lenght:
                current_list.append(current_string)
                global_list.append(current_list)
                current_list = []
                current_string = word[:]
                current_list.append(current_string)
                global_list.append(current_list)
                current_string = ''
                current_list = []
            while len(word) > lenght:
                edge = lenght - len(current_string)
                current_string += word[0:edge]
                current_list.append(current_string)
                word = word[edge:]
                global_list.append(current_list)
                current_list = []
                current_string = ''
                if len(word) <= lenght:
                    current_string += word if len(word) == lenght else word + ' '
                    current_list = []
    if len(current_string) != 0:
        a = [current_string]
        global_list.append(a)
    check_list = []
    word = ''
    if len(subs) > lenght:
        check_list = '0' * len(global_list)
        return list(check_list)
    for i in global_list:
        if ' ' not in i[0]:
            check_list.append(1) if subs == i[0] else check_list.append(0)
        else:
            if subs in i[0]:
                check = i[0]
                for k in range(0, len(check)):
                    if check[k] != ' ':
                        word += check[k]
                    elif k == (len(check) - 1):
                        word += check[k] if check[k] != ' ' else ''
                        check_list.append(1) if word == subs else check_list.append(0)
                        word = ''
                    else:
                        if word == subs:
                            check_list.append(1)
                            break
                        else:
                            word = ''
            else:
                check_list.append(0)

    return check_list

