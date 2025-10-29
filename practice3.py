list_a = [1, 2, 3]
list_b = ['A', 'B', 'C']


def zigzag_merge(list_1, list_2):
    zigzag = []
    step = 0
    while step < len(list_1 )  or step < len(list_2) :
        zigzag.append(list_1[step])
        zigzag.append(list_2[step])
        step += 1

    return zigzag

print(zigzag_merge(list_a, list_b))

list_c = [1, 2, 99, -2]
list_d = ['A', 'B', 'C', 'D', 'K']


def zigzag_merge(list_3, list_4):
    zigzag = []
    step = 0
    while step < len(list_3 )  or step < len(list_4) :
        if step < len(list_3) :
            zigzag.append(list_3[step])

        if step < len(list_4):
            zigzag.append(list_4[step])
        step += 1

    return zigzag

print(zigzag_merge(list_c, list_d))