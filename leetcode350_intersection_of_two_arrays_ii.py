# -- coding: utf-8 --
# @Time : DATEDATE{TIME}
# @Author : Mcode
"""
给定两个数组，编写一个函数来计算它们的交集。
方法1是使用一个临时列表进行对比.
方法2-4都是字典统计对比
方法5是排序后使用双指针对比
"""
def intersect(nums1, nums2):
    """
    使用临时列表存储相同的元素,
    每次选取nums1中的一个元素,对nums2进行遍历对比
    如果两者元素相同,则弹出nums2中的元素.
    时间复杂度为n^2
    :param nums1:
    :param nums2:
    :return:
    """
    tmp_list = []
    for item_1 in nums1:
        tmp_list = []
        for item_1 in nums1:
            i = 0
            while i < len(nums2):
                tmp = nums2[i]
                if item_1 == tmp:
                    tmp_list.append(tmp)
                    nums2.pop(i)
                    break
                i += 1
        return tmp_list


nums1 = [1, 2, 3, 4, 5, 6, 7]
nums2 = [2, 5, 7]
print(intersect(nums1, nums2))


def intersect_2(nums1, nums2):
    """
    使用两个临时字典记录元素次数,
    然后根据两个记录判断拼接成最终列表.
    速度很快,但是空间开销非常大.
    :param nums1:
    :param nums2:
    :return:
    """
    tmp_dict_1 = {}
    tmp_dict_2 = {}
    tmp_list = []

    for i in nums1:
        tmp_dict_1[i] = tmp_dict_1.get(i, 0) + 1
    for i in nums2:
        tmp_dict_2[i] = tmp_dict_2.get(i, 0) + 1

    for k, v in tmp_dict_1.items():
        if k in tmp_dict_2:
            tmp_list_2 = []
            tmp = tmp_dict_2[k]
            if v < tmp:
                tmp_list_2.append(k)
                tmp_list = tmp_list + tmp_list_2 * v
            else:
                tmp_list_2.append(k)
                tmp_list = tmp_list + tmp_list_2 * tmp
    return tmp_list


nums1 = [1, 2, 3, 4, 5, 6, 7]
nums2 = [2, 5, 7]
print(intersect_2(nums1, nums2))


def intersect_3(num1, nums2):
    """
    方法三在方法二的基础上进行改进,将nums1计数,遍历nums2中的元素,
    如果字典里存在,而且计数不为0,就将该元素添加到临时列表里,并且计数-1.
    :param num1:
    :param nums2:
    :return:
    """
    tmp_dict_1 = {}
    tmp_list = []
    for i in nums1:
        tmp_dict_1[i] = tmp_dict_1.get(i, 0) + 1
    for num in nums2:
        if num in tmp_dict_1 and tmp_dict_1[num] != 0:
            tmp_list.append(num)
            tmp_dict_1[num] -= 1
    return tmp_list


nums1 = [1, 2, 3, 4, 5, 6, 7]
nums2 = [2, 5, 7]
print(intersect_3(nums1, nums2))


def intersect_4(nums1, nums2):
    """
    方法4是方法3的改进版,如果字典计数为0,着删除这个key,可以加快字典检索速度.
    同时,选择将短一些的列表进行哈希.可以节约空间.
    选择将较长的列表进行哈希,可以解决时间.
    :param nums:
    :param nums2:
    :return:
    """
    if len(nums1) > len(nums2):
        return intersect_4(nums2, nums1)

    tmp_dict_1 = {}
    tmp_list = []
    for i in nums1:
        tmp_dict_1[i] = tmp_dict_1.get(i, 0) + 1
    for num in nums2:
        if num in tmp_dict_1 and tmp_dict_1[num] != 0:
            tmp_list.append(num)
            tmp_dict_1[num] -= 1
            if tmp_dict_1[num] == 0:
                tmp_dict_1.pop(num)
    return tmp_list


nums1 = [1, 2, 3, 4, 5, 6, 7]
nums2 = [2, 5, 7]
print(intersect_4(nums1, nums2))


def intersect_5(nums1, nums2):
    """
    方法5 是通过排序后使用双指针法进行判断.
    :param nums1:
    :param nums2:
    :return:
    """
    nums1.sort()
    nums2.sort()
    length1, length2 = len(nums1), len(nums2)
    index1 = index2 = 0
    tmp_list = []
    while index1 < length1 and index2 < length2:
        if nums1[index1] < nums2[index2]:
            index1 += 1
        elif nums1[index1] > nums2[index2]:
            index2 += 1
        elif nums1[index1] == nums2[index2]:
            tmp_list.append(nums1[index1])
            index1 += 1
            index2 += 1
    return tmp_list


nums1 = [1, 2]
nums2 = [1, 1]
print(intersect_5(nums1, nums2))
