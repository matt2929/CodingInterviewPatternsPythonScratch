from typing import Optional


class SingleLinkedListNode:

    def __init__(self, val: int, next: Optional['SingleLinkedListNode']):
        self.val = val
        self.next = next

    def linked_list_as_array_str(self) -> str:
        parts = ["["]  # Start with the opening bracket
        current = self
        while current:
            parts.append(str(current.val))  # Add the current value as a string
            if current.next:
                parts.append(", ")  # Add a comma and space if there's a next node
            current = current.next
        parts.append("]")  # Add the closing bracket
        return "".join(parts)  # Join all parts into a single string

class DoubleLinkedListNode:

    def __init__(self, val: int, next: Optional['DoubleLinkedListNode'], previous: Optional['DoubleLinkedListNode']):
        self.val = val
        self.next = next
        self.previous = previous


