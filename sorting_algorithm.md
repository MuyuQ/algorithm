# 排序算法

# Mcode

## 排序算法的关键指标

1. **时间复杂度**：衡量算法执行时间随输入规模增长的变化趋势。
2. **空间复杂度**：衡量算法执行过程中所需额外存储空间随输入规模增长的变化趋势。
3. **稳定性**：对于序列中的相同元素，如果排序之后它们的相对位置没有发生改变，则称该排序算法为「稳定排序」，反之则为「不稳定排序」。
4. **是否原地排序**：算法是否只需要常数级的额外空间。

## 选择排序

### 代码实现

```python
from typing import List

def selection_sort(nums: List[int]) -> None:
    """
    选择排序
    :param nums: 待排序的整数列表（原地修改）
    """
    n = len(nums)
    sorted_index = 0
    while sorted_index < n:
        min_index = sorted_index
        for i in range(sorted_index, n):
            if nums[i] < nums[min_index]:
                min_index = i
        nums[sorted_index], nums[min_index] = nums[min_index], nums[sorted_index]
        sorted_index += 1
```

### 算法特性

- **时间复杂度**：O(n²)
- **空间复杂度**：O(1)
- **稳定性**：不稳定排序
  示例：`[5,8,5,2,9]`
  第一次交换 → `[2,8,5,5,9]`
  第二次交换 → `[2,5,8,5,9]`
  原始序列中两个5的相对位置改变
- **原地排序**：是

## 冒泡排序
选择排序失去稳定性的原因是 每次都要交换最小元素(nums[minIndex])和当前元素(nums[sortedInde]),这样会改变相同元素的相对位置.
为了解决这个问题,可以让nums[sortedIndex....minIndex]的元素都往后移动一位,把nums[sortedIndex+1]的位置空出来,放置nums[sortedIndex].
