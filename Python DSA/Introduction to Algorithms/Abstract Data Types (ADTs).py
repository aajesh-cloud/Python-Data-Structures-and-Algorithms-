class Counter:
    def __init__(self):
        self.history = [0]
    def increment(self):
        self.history.append(self.history[-1] + 1)
    def decrement(self):
        self.history.append(self.history[-1] - 1)
    def get_value(self):
        return self.history[-1]
    def reset(self):
        self.history.append(0)
counter = Counter()
counter.increment()
counter.increment()
counter.decrement()
print("Current value:", counter.get_value())
counter.reset()
print("After reset:", counter.get_value())