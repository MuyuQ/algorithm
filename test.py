# -- coding: utf-8 --
# @Time : DATEDATE{TIME}
# @Author : Mcode
nums = [1,2,3,4,5,6,7,8,9]
def rotate(nums, k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    tmp_list = []
    for i in range(k):
        tmp = nums.pop()
        tmp_list.append(tmp)
    nums_tmp = tmp_list + nums
    nums = nums_tmp
rotate(nums,3)
print(nums)