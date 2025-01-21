# Create a doubly linked list
# 创建一个双向链表
class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        # linked_list head
        # 链表头指针, 初始化为None
        self.__head = None
        # linked_list tail
        # 链表的尾指针, 初始化为None
        self.__tail = None
        # 定义链表的长度
        self.size = int(0)


    # Returns the (non-null) Node at the specified element index
    # 返回指定元素索引处的（非空）节点
    def node(self, index):
        self.check_element_index(index)
        # self.size >> 1 Find the middle index value
        if index < (self.size >> 1):
            head = self.__head
            i = int(0)
            while head and i < index:
                head = head.next
                i += 1
            return head
        else:
            tail = self.__tail
            i = self.size - 1
            while tail and i > index:
                tail = tail.previous
                i -= 1
            return tail


    # Check whether the index of the linked list element is legal
    # 检查链表元素的索引是否合法
    def check_element_index(self, index):
        if index < 0 or index >= self.size:
            raise IndexError(f"index: {index} is illegal")


    # linked_list To list
    # 将链表转换为 list
    def to_list(self):
        out = list()
        current = self.__head
        while current:
            out.append(current.data)
            current = current.next
        return out

    # Add new element to end of linked list
    # 在链表末尾插入新节点
    def add_last(self, data):
        # 创建一个新节点
        new_data = Node(data)

        # 如果链表为空, 新节点成为头节点和尾节点
        if not self.__head:
            self.__head = self.__tail = new_data
        else:
            # 将尾节点的 next 指向新节点
            self.__tail.next = new_data
            # 新节点的 prev 指向原尾节点
            new_data.previous = self.__tail
            # 更新现在的尾节点为新节点
            self.__tail = new_data
        self.size += 1

    # Add an element to the beginning of the linked list
    # 在链表开头添加一个元素
    def add_first(self, data):
        # 创建一个新节点
        new_data = Node(data)

        # If the linked list is empty, the new nodes become the head node and tail node
        # 如果链表为空, 新节点成为头节点和尾节点
        if not self.__head:
            self.__head = self.__tail = new_data
        else:
            # 新节点的 next 指向头节点
            new_data.next = self.__head
            # 原头节点 prev 指向新节点
            self.__head.previous = new_data
            # 更新头节点为 新节点
            self.__head = new_data
        self.size += 1


    # Insert element at specified index in linked list
    # 在链表指定index 插入元素
    def insert(self, index, data):
        if index == self.size:
            self.add_last(data)
        else:
            node = self.node(index)
            prev = node.previous
            new_data = Node(data)
            node.previous = new_data
            new_data.next = node
            if prev is None:
                self.__head = new_data
                new_data.previous = self.__head
            else:
                prev.next = new_data
                new_data.previous = prev


    # Delete from the head node
    # 从头节点开始删除
    def remove_first(self):
        self.pop()


    # Return the first node's value and remove it from the list
    # 弹出链表第一个元素
    def pop(self):
        head = self.__head
        element = head.data
        if not head:
            print("linked_list is empty")
            return None
        next = head.next
        # 更新头节点
        self.__head = next
        # 如果链表只有一个元素
        if not next:
            # 链表为空, 尾节点也应该为 None
            self.__tail = None
        else:
            # 头节点的后一个节点的 prev, 指向None
            next.previous = None
        self.size -= 1
        head.data = None
        # 清理头节点的 后一个指针
        head.next = None
        return element

    # Delete starting from the last node
    # 从尾节点开始删除
    def remove_last(self):
        # 如果链表为空, 直接返回
        if not self.__tail:
            print("linked_list is empty")
            return

        tail = self.__tail
        # 得到尾节点的上一个节点
        prev = tail.previous

        # 更新尾节点
        self.__tail = prev
        # 如果链表只有一个元素
        if not prev:
            # 链表为空, 头节点也应该为 None
            self.__head = None
        else:
            # 尾节点的上一个节点的 next, 应该指向None
            prev.next = None
        self.size -= 1
        tail.data = None
        # help gc
        tail.previous = None


    # remove element
    # 删除元素
    def remove(self, data):
        current = self.__head
        while current:
            if current.data == data:
                # 如果当前节点有 previous 节点
                if current.previous:
                    current.previous.next = current.next
                # 如果当前节点有 next 节点
                if current.next:
                    current.next.previous = current.previous
                # 如果当前节点是头结点
                if current == self.__head:
                    self.__head = current.next
                # 如果当前节点是尾节点
                if current == self.__tail:
                    self.__tail = current.previous
                current.data = None
                # help gc
                current.next = None
                current.previous = None
                self.size -= 1
            current = current.next


    # search node data
    # 查找或搜索node中的元素
    def search(self, data):
        current = self.__head
        while current:
            if current.data == data:
                return current

            current = current.next
        return None

    # Print all elements in the linked list, from beginning to end
    # 打印链表中所有的元素, 从头到尾
    def print_list(self):
        current = self.__head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")


    # Print all elements in the linked list, from end to beginning
    # 打印链表中所有的元素, 从尾到头
    def print_reverse_list(self):
        current = self.__tail
        while current:
            print(current.data, end=" <-> ")
            current = current.previous
        print("None")



if __name__ == "__main__":
    linked_list = DoublyLinkedList()
    linked_list.add_last("libaba")
    linked_list.add_last("lixiwen")
    linked_list.add_last("lixin")
    linked_list.add_last("liyirui")
    linked_list.print_list()

    node = linked_list.search("lixiwen")
    print(node.data)

    data_list = linked_list.to_list()
    print(data_list)
    print(linked_list.size)
    print(isinstance(linked_list.size,int))

    assert linked_list.size == 4, f"list contents: {linked_list.to_list()}"

    print(linked_list.pop())
    linked_list.print_list()
    node = linked_list.node(2)
    print(node.data)
    linked_list.insert(2,"dengdafen")
    linked_list.print_list()
