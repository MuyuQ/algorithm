# -- coding: utf-8 --
# @Time : DATEDATE{TIME}
# @Author : Mcode

"""
189.旋转数组
要求空间复杂度为O(1),所以不能使用切片/临时列表等方法.

"""
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def rotate(nums, k):
    """
    依次pop出队列末尾数据,然后通过insert插入到队首.
    pop的时间复杂度为O(1),insert的时间复杂度为O(n)
    :param nums:
    :param k:
    :return:
    """
    for k in range(k):
        tmp = nums.pop()
        nums.insert(0, tmp)
    return nums


print(rotate(nums, 3))


def rotate_2(nums, k):
    """
    将整个列表反转,然后再讲前后两部分分别反转
    方法2虽然达到了效果,但是并不符合题意.
    使用了额外的空间,并不是原地算法
    :param nums:
    :param k:
    :return:
    """
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    nums.reverse()
    tmp_1 = nums[:k]
    tmp_1.reverse()
    tmp_2 = nums[k:]
    tmp_2.reverse()
    nums = tmp_1 + tmp_2
    return nums


print(rotate_2(nums, 3))


def rotate_3(nums, k):
    """
    方法远离同上,不过通过原地反转实现
    :param nums:
    :param k:
    :return:
    """
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    length = len(nums)
    # 如果出现列表长度小于k的情况,会导致index outof range问题,
    # 需要对k的值进行修正(k=lenght的情况是无意义的,因为列表并不会改变)
    # while len(nums) < k:
    #     k = k - length
    # 取余即可
    k = k % length
    def swap(l, r):
        r -= 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    swap(0, length)
    swap(0, k)
    swap(k, length)
    return nums


print(rotate_3(nums, 3))
