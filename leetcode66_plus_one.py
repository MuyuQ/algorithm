# -- coding: utf-8 --
# @Time : DATEDATE{TIME}
# @Author : Mcode


def plus_one(digits):
    """
    str和int相互变换,比较取巧
    :param digits:
    :return:
    """
    tmp = ''
    tmp_list = []
    for i in digits:
        tmp = tmp + str(i)

    for i in str(int(tmp) + 1):
        tmp_list.append(int(i))
    if len(digits) > len(tmp_list):
        tmp_list.insert(0, 0)
    return tmp_list

digits = [1, 2, 3]
print(plus_one(digits))


def plus_one_2(digits):
    """
    使用range(start,stop,step)倒过来处理.
    如果对应的是9,则变为0,并处理大一位,加一,并##直接返回##.
    这里的直接返回是关键.
    :param digits:
    :return:
    """
    length = len(digits)
    for i in range(length - 1, -1, -1):
        if digits[i] != 9:
            digits[i] += 1
            return digits
        else:
            digits[i] = 0
    digits.insert(0, 1)

    return digits

digits = [1, 2, 3]
print(plus_one_2(digits))


def plus_one_3(digits):
    """

    :param digits:
    :return:
    """
    sum = 0
    for i in range(1, len(digits) + 1):
        sum += digits[-i] * 10 ** (i - 1)
    tmp = [int(x) for x in str(sum + 1)]
    # 为了防止出现[0,0]这种情况
    if digits[0] == 0 and len(tmp) < len(digits):
        tmp.insert(0, 0)
    return tmp

digits = [1, 2, 3]
print(plus_one_3(digits))
