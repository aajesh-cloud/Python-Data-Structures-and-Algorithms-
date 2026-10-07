class QueueUsingStacks:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, item):
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(item)
        while self.s2:
            self.s1.append(self.s2.pop())

    def dequeue(self):
        return self.s1.pop()


q = QueueUsingStacks()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.dequeue())
print(q.dequeue())