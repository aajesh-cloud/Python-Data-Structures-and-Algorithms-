class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_front(self, value):
        new_node = Node(value)
        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def display_forward(self):
        current = self.head
        while current is not None:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")


linked_list = DoublyLinkedList()
linked_list.insert_at_front(30)
linked_list.insert_at_front(20)
linked_list.insert_at_front(10)

linked_list.display_forward()