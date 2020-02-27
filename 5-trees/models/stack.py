class Stack():
    def __init__(self):
        self.stack = []

    def add(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        return self.stack == []

    def peek(self):
        return self.stack[-1]
