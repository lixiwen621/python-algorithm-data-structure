class Array:
    def __init__(self, size):
        # 初始化一个固定大小的数组, size为数字的初始化大小
        self.size = size
        self.array = [None] * size
        # 数组中元素的个数
        self.length = 0


    # def __iter__(self):
    #     for item in self.array:
    #         return item


    def __repr__(self):
        return str([v for v in self.array])

    # def __str__(self):
    #     """返回数组的字符串表示"""
    #     return f"Array({self.array[:self.length]})"


    def append(self, value):
        """
        向数组末尾添加一个 value
        :param value:
        :return:
        """
        if self.length < self.size:
            self.array[self.length] = value
            self.length = self.length + 1
        else:
            print("Array is full! Can't append value.")


    def insert(self, index, value):
        """
        向数组指定的索引位置插入 value
        :param index:
        :param value:
        :return:
        """
        self.check_element_index(index)
        if self.length < self.size:
            # index 小于 length , index 后面的元素每个都往后移一位(从数组最后开始操作比较方便)，
            # 然后替换array[index]为 插入的元素
            for i in range(self.length, index, -1):
                self.array[i] = self.array[i - 1]
            self.array[index] = value
            self.length = self.length + 1
        else:
            print("Array is full! Can't append value.")


    def check_element_index(self, index):
        """
        检查元素索引是否合法
        :param index:
        :return:
        """
        if index < 0 or index >= self.size:
            raise IndexError(f"index: {index} is illegal")


if __name__ == "__main__":
    arr = Array(5)
    arr.append(10)
    arr.append(20)
    arr.append(30)
    print(arr)

    arr.insert(1,3)
    arr.insert(3,5)
    print(arr)