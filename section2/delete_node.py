from section2.linked_list import LinkedList


def delete_node(node):
    current = node
    while current is not None and current.next:
        current.value = current.next.value
        if not current.next.next:
            current.next = None
        current = current.next


if __name__ == '__main__':
    test_list = [1, 2, 3, 4, 5, 6]

    ll = LinkedList(test_list)

    node_to_delete = ll.head.next  # 2
    delete_node(node_to_delete)

    assert [1, 3, 4, 5, 6] == ll.to_list()
