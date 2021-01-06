from section2.linked_list import LinkedList, Node


def is_palindrome(ll):
    reverse_list = LinkedList()
    current = ll.head
    while current:
        reverse_list.prepend(Node(current.value))
        current = current.next

    reverse_char = reverse_list.head
    forward_char = ll.head
    while reverse_char and forward_char:
        if reverse_char.value != forward_char.value:
            return False
        reverse_char = reverse_char.next
        forward_char = forward_char.next

    return True


tests = [
    ([1, 2, 3], False),
    ([1, 1, 1], True),
    ([1], True),
    ([1, 2], False),
    ([1, 2, 1], True),
    ([], True)
]

for test in tests:
    ll = LinkedList(test[0])
    assert is_palindrome(ll) == test[1]
