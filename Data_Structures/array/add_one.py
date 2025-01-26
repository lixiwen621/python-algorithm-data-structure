# input = [1, 2, 3]
# output = [1, 2, 4]
def add_one(list):
    str_num = ""
    for num in list:
        str_num = str_num + str(num)

    int_num = int(str_num) + 1
    str_num = str(int_num)
    out = []
    for num in str_num:
        out.append(int(num))

    return out

# 用数组的方式来解决问题
def add_one2(array):
    if not isinstance(array, list):
        raise TypeError("Type must be list")

    for index in range(len(array), 0, -1):
        array[index-1] = int(array[index-1]) + 1
        array[index-1] = array[index-1] % 10
        if array[index-1] % 10 != 0:
            return array

    out = [1]
    for item in array:
        out.append(item)

    return out



def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]

    output = add_one2(arr)
    if solution == output:
        print("Pass")
    else:
        print("Fail")

if __name__ == "__main__":
    # Test Case 1
    arr = [0]
    solution = [1]
    test_case = [arr, solution]
    test_function(test_case)

    # Test Case 2
    arr = [1, 2, 3]
    solution = [1, 2, 4]
    test_case = [arr, solution]
    test_function(test_case)

    # Test Case 3
    arr = [9, 9, 9]
    solution = [1, 0, 0, 0]
    test_case = [arr, solution]
    test_function(test_case)