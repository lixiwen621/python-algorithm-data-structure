# Problem Statement
# You have been given an array containg numbers. Find and return the largest sum in a contiguous subarray within the input array.
# Example 1:
# - arr= [1, 2, 3, -4, 6]
# - The largest sum is 8, which is the sum of all elements of the array.
# - 最大的和是8，这是数组所有元素的和。
#
# Example 2:
# - arr = [1, 2, -5, -4, 1, 6]
# - The largest sum is 7, which is the sum of the last two elements of the array.
# - - 最大和为 7，即数组最后两个元素的和。

# Iterate through all possible subarrays, calculate their sum, and record the largest sum
# 遍历所有可能的子数组，计算它们的和，记录最大的和
# Time complexity: O(n²)
def max_sum_subarray(array):
    max_sum = 0
    for i in range(len(array)):
        current_sum = 0
        for j in range(i, len(array)):
            current_sum += array[j]
            max_sum = max(current_sum,max_sum)
    return max_sum


# Kadane's Algorithm
# 卡丹算法
def max_sum_subarray1(array):
    max_sum = 0
    current_sum = 0
    for num in array:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum



def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]

    output = max_sum_subarray1(arr)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


if __name__ == "__main__":
    arr = [1, 2, 3, -4, 6]
    solution = 8  # sum of array
    test_case = [arr, solution]
    test_function(test_case)

    arr = [1, 2, -5, -4, 1, 6]
    solution = 7  # sum of last two elements
    test_case = [arr, solution]
    test_function(test_case)

    arr = [-12, 15, -13, 14, -1, 2, 1, -5, 4]
    solution = 18  # sum of subarray = [15, -13, 14, -1, 2, 1]
    test_case = [arr, solution]
    test_function(test_case)
