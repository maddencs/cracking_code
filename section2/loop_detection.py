from section2.linked_list import LinkedList


def loop_detection(ll):
    seen = set()
    current = ll.head
    while current:
        if current in seen:
            return current
        seen.add(current)
        current = current.next


ll = LinkedList([1, 2, 3, 4])

loop_start = loop_detection(ll)

assert loop_start is None


loop_node_start = ll.head.next  # 2
tail = ll.head.next.next.next
tail.next = loop_node_start

detected_loop_start = loop_detection(ll)
assert detected_loop_start == loop_node_start



