from models.stack import Stack


def rev_string(string):
    string_stack = Stack()
    for char in string:
        string_stack.add(char)

    reversed_string = ""
    for _ in range(len(string)):
        reversed_string += string_stack.pop()

    return reversed_string


print(rev_string("I am a hippopotomus."))
