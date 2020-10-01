def UFO(N, data, octal):
    new_date = []
    for i in data:
        if octal is True:
            number = int(str(i), 8)
            new_date.append(number)
        if octal is False:
            number = int(str(i), 16)
            new_date.append(number)
    return new_date
