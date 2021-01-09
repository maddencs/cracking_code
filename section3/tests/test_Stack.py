import pytest

from section3.stack import Stack, Node
from section3.stack_sort import StackSort


class TestStack:
    @pytest.fixture(autouse=True)
    def init(self):
        self.stack = Stack()

    def test_push(self):
        node = Node()
        self.stack.push(node)
        assert self.stack.top == node

        node2 = Node()
        self.stack.push(node2)
        assert self.stack.top == node2
        assert self.stack.top.next == node

    def test_peek(self):
        node = Node()
        self.stack.push(node)
        assert self.stack.peek() == node

    def test_is_empty(self):
        assert self.stack.is_empty()

        node = Node()
        self.stack.push(node)
        assert not self.stack.is_empty()

    def test_to_list(self):
        original_list = [1, 2, 3, 4, 5]
        for i in original_list:
            self.stack.push(Node(i))

        as_list = self.stack.to_list()
        expected_list = list(reversed(original_list))
        assert as_list == expected_list

    def test_sort_stack(self):
        unsorted_list = [2, 9, 2, 4, 6, 10, 1]
        sorted_list = sorted(unsorted_list)

        for i in unsorted_list:
            self.stack.push(Node(i))

        StackSort().sort(self.stack)

        sorted_to_list = self.stack.to_list()
        assert sorted_to_list == sorted_list
