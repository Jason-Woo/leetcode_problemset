def solution(n, k):
    """
    :param n: n种不同的数字的牌
    :param k: 手上有k张牌
    :return: 有多少种牌序
    """
    basic = pow(2, 10) + 7
    return iter_solution(n, k) % basic


def iter_solution(n, k):
    if n == 2:
        return k + 1
    else:
        cnt = 0
        for i in range(0, k + 1):
            cnt += iter_solution(n - 1, k - i)
        return cnt
