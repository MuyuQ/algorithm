# -- coding: utf-8 --
# @Time : DATEDATE{TIME}
# @Author : Mcode
nums = [1,2,2,3,3,3]

def single_number(nums):
    """
    虽然可以通过字典计数,但是需要额外的空间复杂度,并不是原地算法.
    :param nums:
    :return:
    """
    dict = {}
    for num in nums:
        if num not in dict:
            dict[num] = 1
        else:
            dict[num] += 1
    for k, v in dict.items():
        if v == 1:
            return k

print(single_number(nums))


def single_number_2(nums):
    """
    第二种方法是第一种的改进版.通过dict.get(key,default)方法,不需要多次遍历字典,大大降低了时间复杂度.

    :param nums:
    :return:
    """
    tmp_dict = {}
    for num in nums:
        tmp_dict[num] = tmp_dict.get(num, 0) + 1
    for k,v in tmp_dict.items():
        if v ==1:
            return k

def single_number_3(nums):
    """
    类似的方法还有collections中的Counter方法
    :param nums:
    :return:
    """
    nums = [1,2,2,3,3,4,1]
    from collections import Counter
    dict = Counter(nums)
    for k,v in dict.items():
        if v == 1:
            return k
print(single_number_3(nums))