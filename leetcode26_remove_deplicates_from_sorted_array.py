# -- coding: utf-8 --
# @Time : DATEDATE{TIME}
# @Author : Mcode
nums = [1, 1, 2]


def remove_deplicates(nums) -> int:
    """
    双指针法,
    如果快慢指针值相同,则通过list.pop方法,
    如果不同,则通过移动快慢指针
    :param nums: 传入的有序列表
    :return: 去重后列表的大小
    """
    i, j = 0, 1
    length = len(nums)
    if length == 0:
        return 0
    while j < len(nums):
        if nums[i] == nums[j]:
            nums.pop(j)
        else:
            j += 1
            i += 1
    return i + 1


"""
上面的方法使用了pop方法导致时间复杂度变成了o(n^2),所以需要进行改变
"""


def remove_deplicates_2(nums) -> int:
    """
    修改前K的数,
    如果遇到两值相等,则快指针进一步.
    如果两值不等,则慢指针+1,同时将快指针的值赋值给慢指针,快指针+1
    1, 2, 3, 3, 4
    
    处理完所有数据后,从依次pop列表末尾数据.
    pop末尾的时间复杂度为o(1)
    pop中间数据的时间复杂度为o(n)
    
    :param nums: 需要处理的列表
    :return: 去重后的列表大小
    """""
    i, j = 0, 1
    length = len(nums)
    if length == 0:
        return 0
    while j < len(nums):
        if nums[i] == nums[j]:
            j += 1
        else:
            i += 1
            nums[i] = nums[j]
            j += 1
    if length > len(nums):
        nums.pop() * (length - i + 1)
    return i + 1
