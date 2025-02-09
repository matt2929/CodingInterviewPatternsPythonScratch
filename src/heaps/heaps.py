import collections
import heapq
from dataclasses import dataclass
from typing import Any, List

from linked_lists.model import SingleLinkedListNode


class Heap:

    def k_most_frequent_str(self, k: int, input_strs: List[str]):
        count_times_present = collections.Counter(input_strs)
        priority_nodes = [MinPriorityNode(priority=v, payload=k) for k, v in count_times_present.items()]
        heap = []
        heapq.heapify(heap)
        for i in priority_nodes:
            if len(heap) == k:
                if heap[0].priority < i.priority:
                    heapq.heappop(heap)
                    heapq.heappush(heap, i)
            else:
                heapq.heappush(heap, i)
        output = [heapq.heappop(heap).payload for _ in range(min(len(priority_nodes), k))]
        output.reverse()
        return output

    def combine_linked_lists(self, input_nodes: List[SingleLinkedListNode]):
        heap = []
        heapq.heapify(heap)
        output_head = SingleLinkedListNode(-1, None)
        running_node = output_head
        for i in input_nodes:
            if i:
                heapq.heappush(heap, MinPriorityNode(priority=i.val, payload=i))
        while heap:
            top_node = heapq.heappop(heap)
            print(f"\nh: {heap}\n\tt: {top_node}")
            running_node.next = SingleLinkedListNode(top_node.priority, None)
            running_node = running_node.next
            if top_node.payload.next:
                heapq.heappush(heap, MinPriorityNode(priority=top_node.payload.next.val, payload=top_node.payload.next))
        return output_head.next

    def find_median(self, input_list: List[int]) -> int:
        left_heap = []
        right_heap = []
        for i in input_list:
            print(
                f"\n\t1:{left_heap} {left_heap[0] if left_heap else None}\n\t2:{right_heap} {right_heap[0] if right_heap else None}")
            if not left_heap or i <= - left_heap[0]:
                heapq.heappush(left_heap, -1 * i)
            else:
                heapq.heappush(right_heap, i)
            if len(left_heap) > len(right_heap)+1:
                heapq.heappush(right_heap, -heapq.heappop(left_heap))
            if len(right_heap) > len(left_heap):
                heapq.heappush(left_heap, -heapq.heappop(right_heap))
        if len(left_heap) > len(right_heap):
            return -heapq.heappop(left_heap)
        else:
            return (-heapq.heappop(left_heap) + (heapq.heappop(right_heap))) / 2


@dataclass
class MinPriorityNode:
    priority: int
    payload: any

    def __lt__(self, other):
        return self.priority < other.priority


@dataclass
class MaxPriorityNode:
    priority: int
    payload: any

    def __lt__(self, other):
        return self.priority > other.priority
