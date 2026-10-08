class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def has_cycle(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


a = Node(1)
b = Node(2)
c = Node(3)
a.next = b
b.next = c
c.next = a

print("Contains cycle:", has_cycle(a))