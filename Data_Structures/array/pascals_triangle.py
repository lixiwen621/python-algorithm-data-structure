# 根据 n 生成 Pascal's Triangle Array
# Row 0:        1
# Row 1:      1   1
# Row 2:     1   2   1
# Row 3:    1   3   3   1
# Row 4:   1   4   6   4   1
# Row 5:  1   5  10  10   5   1
# C(n,k)=C(n−1,k−1)+C(n−1,k), 其中n表示行号 k为列  C(4,2)=C(3,1) + C(3,2)   如上图
def generate_pascals_triangle(n):
    if n == 0:
        return [1]
    current_row = [1]

    # previous_row 为上一行的数组信息, 一定要有上一行数据信息
    for i in range(1, n+1):
        # # Set the `current】_row` from previous iteration as the `previous_row`
        previous_row = current_row

        # Let's build the fresh current_row gradually
        # add the default first element at the 0^th index of the `i^th` row
        # current_row 为新的当前行数组信息
        current_row = [1]
        for j in range(1, i):
            # An element at position `j` in the current row is the
            # sum of elements at position `j` and `j-1` in the previous row.
            next_number = previous_row[j] + previous_row[j-1]
            current_row.append(next_number)
        current_row.append(1)
    return current_row

if __name__ == "__main__":
    triangle = generate_pascals_triangle(4)
    print(triangle)