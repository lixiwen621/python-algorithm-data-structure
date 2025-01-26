# Sorting with Linked Lists
class Node:
    def __init__(self, element):
        self.element = element
        self.next = None


    def __repr__(self):
        return self.element


class SortedLinkedList:
    def __init__(self):
        self.head = None


    def __iter__(self):
        current = self.head
        while current:
            yield current.element
            current = current.next

    def __repr__(self):
        return str([v for v in self])


    def append(self, element):
        new_node = Node(element)
        if self.head is None:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node

    # Sort elements when adding them to the linked list
    # 在添加元素到链表中的时候就进行排序
    def append_sort(self, element):
        new_node = Node(element)
        if self.head is None:
            self.head = new_node
            return

        if element < self.head.element:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        while current.next and element >= current.next.element:
            current = current.next

        new_node.next = current.next
        current.next = new_node


    def to_list(self):
        out = []
        current = self.head
        while current:
            out.append(current.element)
            current = current.next

        return out

    def print_list(self):
        current = self.head
        while current:
            print(current.element, end=" -> ")
            current = current.next


def sort(array):
    linked_list = SortedLinkedList()
    for value in array:
        linked_list.append_sort(value)
    sorted_array = linked_list.to_list()
    return sorted_array



if __name__ == "__main__":
    sort_linked_list = SortedLinkedList()
    sort_linked_list.append_sort(8)
    sort_linked_list.append_sort(6)
    sort_linked_list.append_sort(9)
    sort_linked_list.append_sort(12)
    sort_linked_list.append_sort(5)
    sort_linked_list.append_sort(13)
    sort_linked_list.append_sort(3)

    print(sort_linked_list)
    print("\n")

    my_list = [3,1,2,-1,0]
    sorted_list = sort(my_list)
    print(sorted_list)
