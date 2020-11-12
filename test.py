# -- coding: utf-8 --
# @Time : DATEDATE{TIME}
# @Author : Mcode
nums = [1,0,0,2,3,4,5,6]
def rotate(nums):
    """
    Do not return anything, modify nums in-place instead.
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
print(rotate(nums))