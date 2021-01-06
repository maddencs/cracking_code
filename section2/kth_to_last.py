from section2.linked_list import LinkedList


def get_kth_to_last(linked_list, k):
    kth_to_last = linked_list.head
    current = linked_list.head
    position = 1
    while current:
        if current.next:
            if position >= k:
                kth_to_last = kth_to_last.next
            position += 1
        current = current.next
    return kth_to_last


test_list = [1, 2, 3, 4, 5, 6]
ll = LinkedList(test_list)
tests = [
    (1, 6),
    (2, 5),
    (3, 4),
    (4, 3),
    (5, 2),
    (6, 1),
]

for test in tests:
    assert get_kth_to_last(ll, test[0]).value == test[1]
