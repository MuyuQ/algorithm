# -*- coding: utf-8 -*-
# 排序算法
# Mcode

# 排序算法的关键指标
# 1. 时间复杂度
# 2. 空间复杂度
# 3. 稳定性 
    # 对于序列中的相同元素，如果排序之后它们的相对位置没有发生改变，则称该排序算法为「稳定排序」，
    # 反之则为「不稳定排序」
# 4. 是否原地排序

# 选择排序

def selection_sort(nums: List[int])->None:
    """
    选择排序
    """
    n = len(nums)
    # sorted_index 表示已排序的索引
    sorted_index = 0
    while sorted_index < n:
        # 从待排序的部分中找到最小的元素
        min_index = sorted_index
        for i in range(sorted_index,n):
            if nums[i]  < nums[min_index]:
                min_index = i
        # 将最小的元素放到已排序的部分的最后
        nums[sorted_index],nums[min_index] = nums[min_index],nums[sorted_index]
        sorted_index += 1
    return nums

# 时间复杂度 o(n^2)
# 空间复杂度 o(1)
# 不稳定排序
#    比如[5,8,5,2,9]
#    第一次排序后变成[2,8,5,5,9]
#    第二次排序后变成[2,5,8,5,9]
#    可以看到 5 的相对位置发生了改变
# 原地排序


