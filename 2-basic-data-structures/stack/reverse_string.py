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


def rev_string(string):
    string_stack = Stack()
    for char in string:
        string_stack.add(char)

    reversed_string = ""
    for _ in range(len(string)):
        reversed_string += string_stack.pop()

    return reversed_string


print(rev_string("I am a hippopotomus."))
