class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def merge_sorted_lists(list1, list2):
    dummy = Node(0)
    tail = dummy

    while list1 is not None and list2 is not None:
        if list1.data <= list2.data:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    tail.next = list1 if list1 is not None else list2
    return dummy.next


def display(head):
    while head is not None:
        print(head.data, end=" -> ")
        head = head.next
    print("None")


list1 = Node(1)
list1.next = Node(3)
list1.next.next = Node(5)

list2 = Node(2)
list2.next = Node(4)
list2.next.next = Node(6)

merged = merge_sorted_lists(list1, list2)
display(merged)