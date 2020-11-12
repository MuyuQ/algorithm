# -- coding: utf-8 --
# @Time : DATEDATE{TIME}
# @Author : Mcode

# 快慢指针,双循环,列表pop方法
def move_zeros(nums):
    """
    使用双循环的方法, 性能差到爆炸
    :param nums:
    :return:
    """
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[j] != 0:
                break
        if nums[i] == 0:
            nums[j], nums[i] = nums[i], nums[j]
        i += 1
    return nums
nums = [0,1,0,3,12]
print(move_zeros(nums))


def move_zeros_2(nums):
    """
    使用列表的pop和append方法
    :param nums:
    :return:
    """
    i = 0
    length = len(nums)
    while i < length:
        if nums[i] == 0:
            nums.pop(i)
            nums.append(0)
            length-=1
        else:
            i+=1
    return nums
nums = [0,1,0,3,12]
print(move_zeros(nums))

def move_zeros_3(nums):
    """
    快慢指针,如果快指针处不为0,就将这个值赋给慢指针,慢指针+1.
    :param nums:
    :return:
    """
    slow = 0
    for fast in range(len(nums)):
        if nums[fast]!=0:
            nums[slow]=nums[fast]
            slow+=1
    for i in range(slow,len(nums)):
        nums[i]=0
    return nums
nums = [0,1,0,3,12]
print(move_zeros(nums))

def move_zeros_4(nums):
    """
    zero指向0的最左侧.
    依次遍历,如果不为0,就和zero位置互换.
    :param nums:
    :return:
    """
    zero = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[zero] = nums[zero], nums[i]
            zero += 1