from section2.linked_list import LinkedList


def remove_dups(linked_list):
    current = linked_list.head
    while current:
        remove_doubles(current)
        current = current.next


def remove_doubles(head):
    value = head.value
    prev = head
    current = head.next
    while current:
        if current.value == value:
            prev.next = current.next
            current = prev.next
        else:
            prev = current
            current = current.next


tests = [
    ([1, 2, 3, 4], [1, 2, 3, 4]),
    ([1, 1, 2, 3], [1, 2, 3]),
    ([1, 2, 2, 3], [1, 2, 3]),
    ([1, 2, 3, 3], [1, 2, 3]),
    ([1], [1]),
    ([], []),
]

for test in tests:
    ll = LinkedList(test[0])
    remove_dups(ll)
    assert ll.to_list() == test[1]
