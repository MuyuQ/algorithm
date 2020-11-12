# -- coding: utf-8 --
# @Time : DATEDATE{TIME}
# @Author : Mcode

nums = [1,2,3,4,5,5,7]
def contains_duplicate(nums) ->bool:
    """
    使用set元素不重复的特性,可以非常简单的完成任务
    :param nums:
    :return:
    """
    return not len(set(nums))==len(nums)

print(contains_duplicate(nums))

def contains_duplicate_2(nums) ->bool:
    """
    使用字典存储每个元素的数量,
    :param nums:
    :return:
    """
    dict = {}
    for num in nums:
        if num not in dict:
            dict[num] = 1
        else:
            dict[num] += 1
            return True
    return False

print(contains_duplicate_2(nums))