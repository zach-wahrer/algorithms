from .node import Node


class UnorderedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def __len__(self):
        if self.head:
            counter = 1
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
                counter += 1
            return counter
        else:
            return None

    def add(self, data):
        if self.head:
            temp = self.head
            self.head = Node(data)
            self.head.next = temp
        else:
            new_node = Node(data)
            self.head = new_node
            self.tail = new_node

    def append(self, data):
        if self.tail:
            new_tail = Node(data)
            old_tail = self.tail
            old_tail.next = new_tail
            self.tail = new_tail
        else:
            new_node = Node(data)
            self.head = new_node
            self.tail = new_node

    def index(self, search):
        pos = 0
        pointer = self.head
        while pointer:
            if pointer.data == search:
                return pos
            else:
                pointer = pointer.next
                pos += 1
        return None

    def insert(self, index, data):
        if index == 0:
            insert = Node(data)
            tmp_head = self.head
            self.head = insert
            self.head.next = tmp_head
        else:
            try:
                current = self.head
                ahead = self.head.next

                for _ in range(index - 1):
                    current = ahead
                    ahead = ahead.next
                insert = Node(data)
                current.next = insert
                insert.next = ahead

            except AttributeError:
                raise Exception('Invalid posistion for UnorderedList insert.')

    def pop(self, index):
        if index == 0:
            tmp_head = self.head
            self.head = self.head.next
            return tmp_head.data

        pos = 0
        pointer = self.head
        while pos < index - 1:
            pointer = pointer.next
            pos += 1
        pop_node = pointer.next
        if pointer.next.next:
            pointer.next = pointer.next.next
        else:
            self.tail = pointer

        return pop_node.data

    def to_list(self):
        output = []
        pointer = self.head
        while pointer:
            output.append(pointer.data)
            pointer = pointer.next
        return output
