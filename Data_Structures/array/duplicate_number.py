# Problem Statement
# You have been given an array of length = n. The array contains integers from 0 to n - 2. Each number in the array is present exactly once except for one number which is present twice. Find and return this duplicate number present in the array
#
# Example:
#
# arr = [0, 2, 3, 1, 4, 5, 3]
# output = 3 (because 3 is present twice)
# The expected time complexity for this problem is O(n) and the expected space-complexity is O(1).

# 长度 = n 的数组，该数组包含从0到n-2的整数，数组中每个数字都只出现一次，但有一个数字出现两次
# 找出数组中，重复出现2次的那个元素
# 该问题的预期时间复杂度为 O(n)，预期空间复杂度为 O(1)。

def duplicate_number(array):
    """
    Notice carefully that
    1. All the elements of the array are always non-negative
    2. If array length = n, then elements would start from 0 to (n-2), i.e. Natural numbers 0,1,2,3,4,5...(n-2)
    3. There is only SINGLE element which is present twice.

    Therefore let's find the sum of all elements (current_sum) of the original array, and
    find the sum of first (n-2) Natural numbers (expected_sum).

    Trick:
    The second occurance of a particular number (say `x`) is actually occupying the space
    that would have been utilized by the number (n-1). This leads to:
    current_sum  = 0 + 1 + 2 + 3 + .... + (n-2) + x
    expected_sum = 0 + 1 + 2 + 3 + .... + (n-2)
    current_sum - expected_sum = x
    Tada!!! :)


    仔细注意
    1.数组的所有元素始终为非负数
    2.如果数组长度=n，则元素从0开始到(n-2)，即自然数0,1,2,3,4,5...(n-2)
    3.只有单个元素出现两次。
    因此，让我们找到原始数组的所有元素的总和（current_sum），并且
    求前 (n-2) 个自然数的总和 (expected_sum)。

    窍门：
    特定数字（例如“x”）的第二次出现实际上占用了空间
    这将由数字（n-1）使用。这导致：
    当前总和 = 0 + 1 + 2 + 3 + .... + (n-2) + x         请注意 (当前总和是目前 数组中元素的总和 )
    预期总和 = 0 + 1 + 2 + 3 + .... + (n-2)               请注意(预期总和是 从0开始加到n-2的总和)
    当前总和 - 预期总和 = x
    数字真奇妙
    :param array:
    :return:
    """
    if not isinstance(array, list):
        raise TypeError(f"{array} type is not list")

    current_sum = 0
    expected_sum = 0
    # 计算出 current_sum 的值
    for item in array:
        current_sum += item

    for i in range(len(array)-1):
        expected_sum += i

    return current_sum - expected_sum


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    output = duplicate_number(arr)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


if __name__ == "__main__":
    arr = [0, 0]
    solution = 0
    test_case = [arr, solution]
    test_function(test_case)

    arr = [0, 2, 3, 1, 4, 5, 3]
    solution = 3
    test_case = [arr, solution]
    test_function(test_case)

    arr = [0, 1, 5, 4, 3, 2, 0]
    solution = 0
    test_case = [arr, solution]
    test_function(test_case)

    arr = [0, 1, 5, 5, 3, 2, 4]
    solution = 5
    test_case = [arr, solution]
    test_function(test_case)