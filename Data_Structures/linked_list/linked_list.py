# Create a one-way linked list
# 创建一个单向链表
class Node:
    def __init__(self,data=None):
        # 节点里包含2部分 data和next(下一个data的地址)
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, input_list=None):
        # The head pointer of the linked list, initially None
        # 链表的头指针, 初始为None
        self.head = None

        if input_list and isinstance(input_list, (list, tuple, set, dict)):
            for item in input_list:
                self.append(item)


    def __iter__(self):
        node = self.head
        while node:
            yield node.data
            node = node.next


    def __repr__(self):
        return str([v for v in self])


    def __reversed__(self):
        # Step 1: Collect all elements in a list
        elements = list(self)

        # Step 2: Yield elements in reverse order
        for item in reversed(elements):
            yield item


    # Insert a new node at the end of the linked list
    # 在链表的末尾插入一个新节点
    def append(self, data):
        # Create a new node
        # 创建一个新节点
        new_node = Node(data)
        # If the linked list is empty, the new node becomes the head node
        # 如果链表为空, 新节点成为头节点
        if not self.head:
            self.head = new_node
            return

        last = self.head
        # Find the last node of the linked list
        # 找到链表的最后一个节点
        while last.next:
            last = last.next

        # Link new node after last node
        # 将新节点链接到最后一个节点后面
        last.next = new_node


    # Insert a new node at the beginning of the linked list
    # 在链表开头插入一个新节点
    def prepend(self, data):
        # Create a new node
        # 创建一个新节点
        new_node = Node(data)
        # New node specifies the head node
        # 新节点指定头节点
        new_node.next = self.head
        # Update the head node to the new node
        # 更新头节点为新节点
        self.head = new_node


    # Delete a node in the linked list
    # 删除链表中的一个节点
    def delete(self,key):
        current = self.head
        # If the head node is deleted
        # 如果删除的是头节点
        if current and current.data == key:
            self.head = current.next
            current.data = None
            current.next = None
            return

        # Find the node to delete and keep a reference to the previous node
        # 查找要删除的节点, 并保持对前一个节点的引用
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        # If the node to be deleted is not found
        # 如果未找到要删除的节点
        if current is None:
            return

        prev.next = current.next



    # Print all elements of the linked list
    # 打印链表的所有元素
    def print_list(self):
        current = self.head

        while current:
            print(current.data, end=" ->")
            current = current.next
        # 最后输出None, 表示链表结束
        print("None")


def has_cycle(linked_list):
    fast = linked_list.head
    slow = linked_list.head

    while fast and fast.next:
        # slow 指针每次走一步
        slow = slow.next
        # fast 指针每次走二步
        fast = fast.next.next
        # 如果相遇 说明有环
        if slow == fast:
            return True
    return False


if __name__ == "__main__":
    linked_list = LinkedList([1,2])
    linked_list.append("lixiwen")
    linked_list.append("lixin")
    linked_list.append("liyirui")

