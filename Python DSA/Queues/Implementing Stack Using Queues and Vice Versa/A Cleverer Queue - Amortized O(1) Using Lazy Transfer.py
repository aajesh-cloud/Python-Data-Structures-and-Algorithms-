class EfficientQueue:
    def __init__(self):
        self.inbox = []
        self.outbox = []

    def enqueue(self, item):
        self.inbox.append(item)

    def dequeue(self):
        if not self.outbox:
            while self.inbox:
                self.outbox.append(self.inbox.pop())
        return self.outbox.pop()


q = EfficientQueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.dequeue())
q.enqueue(4)
print(q.dequeue())
print(q.dequeue())