class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse_list(head):
    previous = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node

    return previous


def display(head):
    current = head
    while current is not None:
        print(current.data, end=" -> ")
        current = current.next
    print("None")


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

print("Original: ", end="")
display(head)

head = reverse_list(head)

print("Reversed: ", end="")
display(head)