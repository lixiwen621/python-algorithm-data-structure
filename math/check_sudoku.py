# Check if the n*n list satisfies Sudoku
# The rules of Sudoku:
#   1.The numbers in each row cannot be repeated
#   2.The numbers in each column cannot be repeated
# 检查 n*n list 是不是满足数独
def check_sudoku(square):
    square_column = len(square)
    square_row = len(square[0])
    if square_row == 0 or square_column == 0:
        print("The square list you entered is empty")
        return False
    if square_row != square_column:
        print("You are not entering a square list")
        return False
    for row in square:
        # Create a list with the integers 1, 2, ..., n.
        # We will check that each number in the row is in the list
        # and remove the numbers from the list once they are verified
        # to ensure that each number only occurs once in the row.
        # 创建一个包含整数1,2，…的列表。, n。
        # 我们将检查行中的每个数字是否在列表中
        # #并在验证后将数字从列表中删除
        # #确保每个数字在行中只出现一次。
        check_list = list(range(1,square_row + 1))
        # 检查每一行的数
        for i in row:
            if i not in check_list:
                return False
            check_list.remove(i)
    # 检查每一列
    for n in range(square_column):
        # We do the same here for each column in the square.
        # 我们对正方形中的每一列都做同样的处理。
        check_list = list(range(1,square_row + 1))
        for row in square:
            if row[n] not in check_list:
                return False
            check_list.remove(row[n])
    return True


# 一个合法的 3x3 数独解
sudoku = [
    [1, 2, 3],
    [3, 1, 2],
    [2, 3, 1]
]

# 一个不合法的 3x3 数独（重复数字）
invalid_sudoku = [
    [1, 2, 3],
    [1, 3, 2],
    [2, 3, 1]
]

if __name__ == '__main__':
    print(check_sudoku(sudoku))
    print(check_sudoku(invalid_sudoku))


