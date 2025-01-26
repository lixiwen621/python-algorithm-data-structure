# Linked list class containing child linked lists
# 含有子链表的链表类(单向)
class Node:
    def __init__(self, element):
        self.element = element
        # 指向主链表下一个节点
        self.next = None
        # 指向子链表的头节点
        self.child = None


class MultilevelLinkedList:
    def __init__(self):
        self.head = None


    def __iter__(self):
        node = self.head
        while node:
            yield node.element
            node = node.next


    # 添加到主链表的末尾
    def append_to_main_list(self, element):
        """
        添加节点到主链表
        :param element:
        :return:
        """
        new_node = Node(element)
        last = self.head
        if self.head is None:
            self.head = new_node
        else:
            while last.next:
                last = last.next
            last.next = new_node
        # 返回新节点以便添加子链表
        return new_node


    def append_to_child(self, parent_node, element):
        """
        添加节点到指定父节点的子链表
        :param parent_node:
        :param element:
        :return:
        """
        if parent_node is None:
            raise ValueError("Parent node cannot be None")

        new_node = Node(element)
        if parent_node.child is None:
            parent_node.child = new_node
        else:
            child_current = parent_node.child
            while child_current.next:
                child_current = child_current.next
            child_current.next = new_node
        return new_node


    # 打印多层链表
    def print_list(self):
        """
        打印多层链表, 包括主链表和子链表
        :return:
        """
        def print_node(node, level=0):
            while node:
                print("  " * level + f"Node({node.element})")
                if node.child:
                    print_node(node.child, level + 1)
                node = node.next

        print_node(self.head)

    def print_list2(self, node=None, indent=0, is_child=False):
        """
        打印多层链表。
        :param node: 当前链表的头节点
        :param indent: 当前缩进的空格数
        :param is_child: 是否是子链表
        """
        if node is None:
            node = self.head

        current = node
        first_line = []
        child_lines = []

        while current:
            # 打印当前层的节点
            first_line.append(f"{' ' * indent}{current.element}")
            # 如果有子链表，递归处理
            if current.child:
                child_lines.append(f"{' ' * indent}|")  # 添加竖线表示子链表开始
                child_lines.append(self.print_list2(current.child, indent + 4, True))  # 缩进处理子链表
            current = current.next

        # 拼接当前层和子链表的打印内容
        output = " -> ".join(first_line)
        if child_lines:
            output += "\n" + "\n".join(child_lines)

        # 子链表需要额外缩进
        if is_child:
            return output
        else:
            print(output)


# 扁平化链表(通过递归的方式)
def _flatten(linked_list):
    if not linked_list:
        return
    # 递归的方式查找所有的子链表
    def _flatten_child(child_head):
        while child_head:
            new_linked_list.append_to_main_list(child_head.element)
            if child_head.child:
                _flatten_child(child_head.child)
            child_head = child_head.next

    new_linked_list = MultilevelLinkedList()
    head = linked_list.head
    while head:
        new_linked_list.append_to_main_list(head.element)
        if head.child:
            child_head = head.child
            _flatten_child(child_head)
        head = head.next

    return new_linked_list


# 非递归方法（使用栈）



if __name__ == "__main__":
    mll = MultilevelLinkedList()
    mll2 = MultilevelLinkedList()
    node1 = mll.append_to_main_list("libaba")
    node2 = mll.append_to_main_list("lixiwen")
    node3 = mll.append_to_main_list("lixin")

    node21 = mll.append_to_child(node2,2)
    node22 = mll.append_to_child(node2,3)
    node23 = mll.append_to_child(node2,4)

    node211 = mll.append_to_child(node21,7)
    node212 = mll.append_to_child(node21,8)
    node213 = mll.append_to_child(node21,9)


    mll.print_list()
    print("\n")
    flatten_linked_list = _flatten(mll2)
    flatten_linked_list.print_list()
