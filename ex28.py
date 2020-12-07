def list_of_doors(k : int):
    door = '1 ' * k
    door = door[:-1]
    doors = door.split(' ')
    return doors


def string_of_doors(doors : list):
    door = ''.join(doors)
    return door


def Keymaker(k : int):
    step = 1
    doors = list_of_doors(k)
    for i in range(1,k):
        for j in range(i,k,step+1):
            doors[j] = '0' if doors[j] == '1' else '1'
        step += 1
    door = string_of_doors(doors)
    return door


#https://skillsmart.ru/algo/lvl1/oo0b.html