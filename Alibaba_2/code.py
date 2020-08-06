def distance(a, b):
    """
    :param a: 序列a
    :param b: 序列b
    :return: a到b需要的变换数
    """
    if a == b:
        return 0
    if len(a) == len(b) == 2:
        return 1
    tmp_dis = []
    head = a[0]
    tail = a[-1]
    for i in range(len(b)):
        if b[i] == head:
            tmp_dis.append(distance(a[1:], b[0:i] + b[i + 1:]))

        if b[i] == tail:
            tmp_dis.append(distance(a[:-1], b[0:i] + b[i + 1:]))

    return min(tmp_dis) + 1


if __name__ == '__main__':
    a = 'abcd'
    b = 'badc'
    print(distance(a, b))