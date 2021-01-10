import pytest

from section4.queue import Queue, Node


class TestQueue:
    @pytest.fixture(autouse=True)
    def init(self):
        self.queue = Queue()

    def test_enqueue(self):
        node = Node()
        self.queue.enqueue(node)
        assert self.queue.front == node
        assert self.queue.tail == node

        node2 = Node()
        self.queue.enqueue(node2)
        assert self.queue.front == node
        assert self.queue.tail == node2
        assert self.queue.front.next == node2

        node3 = Node()
        self.queue.enqueue(node3)
        assert self.queue.tail == node3
        assert self.queue.front.next == node2
        assert self.queue.front.next.next == node3

    def test_dequeue(self):
        node1 = Node()
        node2 = Node()

        self.queue.enqueue(node1)
        self.queue.enqueue(node2)

        dequeued = self.queue.dequeue()
        assert dequeued == node1
        assert self.queue.front == node2

        dequeued2 = self.queue.dequeue()
        assert dequeued2 == node2
        assert self.queue.front is None
        assert self.queue.tail is None

    def test_is_empty(self):
        assert self.queue.is_empty()

        node = Node()
        self.queue.enqueue(node)
        assert not self.queue.is_empty()