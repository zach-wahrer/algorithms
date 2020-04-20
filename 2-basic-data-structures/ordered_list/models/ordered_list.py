from .node import Node


class OrderedList():
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
            if data < self.head.data:
                new_node = Node(data)
                tmp_head = self.head
                self.head = new_node
                self.head.next = tmp_head
            else:
                pointer = self.head
                while pointer.next and data > pointer.next.data:
                    pointer = pointer.next

                insert = Node(data)
                ahead = pointer.next
                pointer.next = insert
                insert.next = ahead
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

    def remove(self, item):
        if self.index(item) == 0:
            tmp_head = self.head
            self.head = self.head.next
            return tmp_head.data

        pointer = self.head
        while pointer.next.data != item:
            pointer = pointer.next

        if pointer.next.next:
            pointer.next = pointer.next.next
        else:
            pointer.next = None
            self.tail = pointer

    def search(self, item):
        pointer = self.head
        while pointer:
            if pointer.data == item:
                return True
            if pointer.data > item:
                return False
            pointer = pointer.next
        return False

    def to_list(self):
        output = []
        pointer = self.head
        while pointer:
            output.append(pointer.data)
            pointer = pointer.next
        return output
