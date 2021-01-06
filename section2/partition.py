from section2.linked_list import LinkedList


def partition(ll, partition_value):
    prev = ll.head
    current = ll.head.next
    while current:
        if current.value < partition_value:
            tmp = current.next
            current.next = ll.head
            ll.head = current
            current = tmp
            prev.next = current
        else:
            prev = current
            current = current.next


test_list = [3, 5, 8, 5, 10, 2, 1]

for num in test_list:
    ll = LinkedList(test_list)
    partition(ll, num)
    print(f'Partition Value: {num}\n'
          f'Partitioned List: {ll.to_list()}')

