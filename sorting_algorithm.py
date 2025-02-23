# -*- coding: utf-8 -*-
# 排序算法
# Mcode

# 排序算法的关键指标
# 1. 时间复杂度
# 2. 空间复杂度
# 3. 稳定性
# 4. 是否原地排序

# 选择排序

def selection_sort(nums: List[int])->None:
    """
    选择排序
    """
    n = len(nums)

    sorted_index = 0