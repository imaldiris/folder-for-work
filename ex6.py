import math
def PatternUnlock(n, hits):
    result = 0
    button1 = 0
    button2 = 0
    cord_list = [1, [3, 2],
                 2, [2, 2],
                 3, [1, 2],
                 4, [1, 1],
                 5, [2, 1],
                 6, [3, 1],
                 7, [1, 3],
                 8, [2, 3],
                 9, [3, 3]]
    for i in range(0, n - 1):
        button1 = hits[i]
        button2 = hits[i+1]
        x1 = cord_list[cord_list.index(button1)+1]
        x2 = cord_list[cord_list.index(button2)+1]
        result += math.sqrt(math.fabs(x2[0] - x1[0]) + math.fabs(x2[1] - x1[1]))
    result = str(float('{:.5f}'.format(result)))
    key = ''
    for i in result:
        if i != '0' and i != '.':
            key += i
    return key
