from section2.linked_list import LinkedList, Node


def sum_lists(l1, l2):
    sum_list = LinkedList()
    current1 = l1.head
    current2 = l2.head
    carry = 0
    while current1 and current2:  # TODO: Different length numbers
        current_sum = current1.value + current2.value + carry
        remainder = current_sum % 10
        carry = 1 if current_sum >= 10 else 0
        sum_node = Node(remainder)
        sum_list.append(sum_node)
        current1 = current1.next
        current2 = current2.next

    return sum_list


a = [7, 1, 6]
b = [5, 9, 2]
c = [2, 1, 9]

list_a = LinkedList(a)
list_b = LinkedList(b)

list_sum = sum_lists(list_a, list_b)

assert list_sum.to_list() == c
