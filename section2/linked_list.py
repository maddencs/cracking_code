class LinkedList:
    head = None

    def __init__(self, iterable=None):
        if iterable:
            for i in iterable:
                self.append(Node(i))

    def append(self, node):
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def print(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def to_list(self):
        as_list = list()
        current = self.head
        while current:
            as_list.append(current.value)
            current = current.next

        return as_list


class Node:
    value = None
    next = None

    def __init__(self, value):
        self.value = value


if __name__ == '__main__':
    test1 = [1, 2, 3]

    ll = LinkedList(test1)

    ll.print()

    print(ll.to_list())

