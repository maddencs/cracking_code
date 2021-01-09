class Stack:
    top = None

    def peek(self):
        return self.top

    def pop(self):
        tmp = self.top
        if self.top is not None:
            self.top = self.top.next

        return tmp

    def push(self, node):
        node.next = self.top
        self.top = node

    def is_empty(self):
        return self.top is None

    def to_list(self):
        as_list = list()
        current = self.top
        while current:
            data = current.data
            as_list.append(data)
            current = current.next

        return as_list


class Node:
    data = None
    next = None

    def __init__(self, data=None):
        self.data = data
