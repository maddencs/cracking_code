from section2.linked_list import LinkedList


def get_intersection(l1, l2):
    l1_tail, l1_size = get_tail_and_size(l1)
    l2_tail, l2_size = get_tail_and_size(l2)

    if l1_tail != l2_tail:
        return False

    l1_size_diff = l1_size - l2_size
    l2_size_diff = l2_size - l1_size

    l1_head = get_equal_head(l1, l1_size_diff)
    l2_head = get_equal_head(l2, l2_size_diff)

    l1_current = l1_head
    l2_current = l2_head
    while l1_current and l2_current:
        if l1_current == l2_current:
            return l1_current

        l1_current = l1_current.next
        l2_current = l2_current.next


def get_tail_and_size(ll):
    size = 0
    current = ll.head
    tail = current
    while current:
        size += 1
        tail = current
        current = current.next

    return tail, size


def get_equal_head(ll, size_diff):
    current_offset = size_diff
    head = ll.head

    while current_offset > 0 and head:
        head = head.next
        current_offset -= 1

    return head


l1 = LinkedList([1, 2, 3, 4])
l2 = LinkedList([4, 5, 6])

link_node = l1.head.next  # 2
l2.append(link_node)

intersection = get_intersection(l1, l2)
assert intersection == link_node


l1 = LinkedList([1, 2, 3, 4])
l2 = LinkedList([4, 5, 6])

intersection = get_intersection(l1, l2)
assert not intersection
