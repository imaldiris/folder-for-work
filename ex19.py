def check_string(string):
    """Принимает строку с названием и колличеством, влзвращает имя товара без пробела"""
    sign_string = ''
    numbers = '1234567890'
    for i in string:
        if i not in numbers:
            sign_string += i
        if i in numbers:
            break
    return sign_string


def sorting(list_of_result=list):
    """Принимает список и возвращает соритрованный список по колличеству и названию"""
    item = {}
    for i in range(0, len(list_of_result), 2):
        item.update({list_of_result[i]: list_of_result[i+1]})
    sorted_item = sorted(item.items(), key=lambda x: (-x[1], x[0]))
    item = []
    for i in sorted_item:
        name = i[0] + str(i[1])
        item.append(name)
    return item


def ShopOLAP(n, items):
    result = []
    while len(items) != 0:
        item = items[0]
        items = items[1:]
        copy_items = items[:]
        full_name_of_item = item[0:item.index(' ')+1]
        result_of_current_sale = int(item[item.index(' ')+1:])
        name_of_item = check_string(item)
        sub_list = [full_name_of_item, result_of_current_sale]
        for i in copy_items:  # перебор всех следующих продаж и сравнение с текущей
            current = i[0:len(name_of_item)]
            if current == name_of_item:
                name = i[:i.index(' ') + 1]
                quanity = int(i[i.index(' ') + 1:])
                if name not in sub_list:  # обновление sub_list новыми элементами
                    sub_list.append(name)
                    sub_list.append(quanity)
                else:  # увеличение колличества имеющихся элементов
                    sub_list[sub_list.index(name) + 1] += quanity
                items.remove(i)
        copy_items = items[:]
        result += sub_list
    goods = sorting(result)
    return goods
