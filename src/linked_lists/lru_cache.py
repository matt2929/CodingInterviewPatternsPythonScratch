"""
Design and implement a data structure for the Least Recently Used LRU cache that supports the following operations:

LRUCache (capactiy: int): Initialize an LRU cache with the specified capactiy
get(key: int ) -> int return the value associated with a key. Return -1 if the key doesn't exist.
put (key: int, value Int) -> None add a key and its value to the cache.
If adding element.
IF they key allready exists in the cache update its value.

"""
from linked_lists.model import SingleLinkedListNode, DoubleLinkedListNode
from typing import Mapping, Optional


class LRUCache:

    def __init__(self, capacity: int):
        self.node_mapping: Mapping[int, DoubleLinkedListNode] = {}
        self.head_node = DoubleLinkedListNode(None, None, None, None)
        self.tail_node = self.head_node
        if capacity > 1:
            for i in range(capacity - 1):
                self.tail_node.next = DoubleLinkedListNode(None, None, self.tail_node, None)
                self.tail_node = self.tail_node.next

    def get(self, key: int) -> Optional[int]:
        if target_node := self.node_mapping.get(key):
            # update recentness if not allready most recent
            if target_node != self.head_node:
                self._remove_from_dll_(target_node)
                self._add_to_head_(target_node)
            return target_node.val
        else:
            return None

    def put(self, key: int, value: int) -> None:
        if key in self.node_mapping:
            target_node = self.node_mapping.get(key)
            target_node.val = value
            # update recentness if not allready most recent
            if target_node != self.head_node:
                self._remove_from_dll_(target_node)
                self._add_to_head_(target_node)
        # must evict
        else:
            new_head = DoubleLinkedListNode(key, value, None, self.head_node)
            self.head_node.previous = new_head
            self.head_node = new_head
            self._trim_tail()
        self.node_mapping[key] = self.head_node

    def _remove_from_dll_(self, dlln: DoubleLinkedListNode):
        temp_prev = dlln.previous
        temp_next = dlln.next
        if temp_prev != None:
            temp_prev.next = temp_next
        if temp_next != None:
            temp_next.previous = temp_prev
        dlln.next = None
        dlln.previous = None

    def _trim_tail(self):
        if self.tail_node.key in self.node_mapping:
            del self.node_mapping[self.tail_node.key]
        self.tail_node = self.tail_node.previous
        self.tail_node.next = None

    def _add_to_head_(self, dlln: DoubleLinkedListNode):
        dlln.previous = None
        dlln.next = self.head_node
        self.head_node.previous = dlln
        self.head_node = dlln

    def print_what_look_like(self):
        iter_node = self.head_node
        output = "[\n"
        while (iter_node != None):
            output += f"\t- (k: {iter_node.key} v: {iter_node.val})\n"
            iter_node = iter_node.next
        output += "]"
        print(output)
