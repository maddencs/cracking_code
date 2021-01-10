class Queue:
    front = None
    tail = None

    def enqueue(self, node):
        if self.tail:
            self.tail.next = node

        self.tail = node

        if not self.front:
            self.front = node

    def dequeue(self):
        tmp = self.front
        self.front = self.front.next

        if tmp == self.tail:
            self.tail = None

        return tmp

    def is_empty(self):
        return self.front is None



class Node:
    data = None
    next = None

    def __init__(self, data=None):
        self.data = data