class ListNode:
    def __init__(self, value: int | None = None) -> None:
        self.value = value
        self.next = None

    def __repr__(self) -> str:
        return f"{self.value} -> {self.next}"


class LinkedList:
    def __init__(self, value: int | None) -> None:
        self.head = ListNode(value)

    def append(self, value: int | None) -> None:
        new_node = ListNode(value)
        last_node = self.head

        while last_node.next is not None:
            last_node = last_node.next

        last_node.next = new_node

    def reverse_list(self) -> None:
        prev_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node

    def __repr__(self) -> str:
        return str(self.head)


# Create and reverse a linked list
linked_list = LinkedList(10)
[linked_list.append(value) for value in (20, 30, 40)]
print("Initial linked list:", linked_list)

linked_list.reverse_list()
print("Reversed linked list:", linked_list)
