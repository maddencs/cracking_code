from section3.stack import Stack


class StackSort:
    def sort(self, stack):
        temp_stack = Stack()
        while not stack.is_empty():
            prev, smallest = self._find_smallest(stack)

            if prev:
                prev.next = smallest.next
            else:
                stack.top = smallest.next

            temp_stack.push(smallest)

        self.swap_stacks(temp_stack, stack)

    def _find_smallest(self, stack):
        if stack.is_empty():
            return None

        current = stack.top.next
        if not current:
            return None, stack.top

        prev = stack.top
        smallest_prev = None

        smallest = stack.top
        while current:
            if current.data < smallest.data:
                smallest_prev = prev
                smallest = current

            prev = current
            current = current.next

        return smallest_prev, smallest

    def swap_stacks(self, old_stack, new_stack):
        current = old_stack.pop()
        while current:
            new_stack.push(current)
            current = old_stack.pop()
