import time


def three_change(l):
    while l[0] > l[1] or l[0] > l[2]:
        l[0], l[1], l[2] = l[1], l[2], l[0]
    return l


def check(array, time_start, time_end):
    max = array[0]
    key = False
    for i in range(1, len(array)):
        if array[i] > max:
            key = True
            max = array[i]
        else:
            return False
    if time_end - time_start < 1 and key is True:
        return True
    else:
        return False


def MisterRobot(n, data):
    time_start = time.monotonic()
    a = data[:]
    count = 0
    for i in range(0, n - 2):
        slice = three_change(a[i:i+3])
        a[i], a[i+1], a[i+2] = slice[0], slice[1], slice[2]
        if i != 0 and a[i] < a[i-1]:
            for k in range(i, 0, -1):
                if a[k] < a[k-1]:
                    slice = three_change(a[k-1:k+2])
                    a[k-1], a[k], a[k+1] = slice[0], slice[1], slice[2]
                    count += 1
            current = i + 1 - count
            if a[current] > a[current + 1]:
                for k in range(current,i+1):
                    slice = three_change(a[k:k+3])
                    a[k], a[k+1], a[k+2] = slice[0], slice[1], slice[2]
        count = 0
    check_time = time.monotonic()
    key = check(a,time_start, check_time)
    return key

