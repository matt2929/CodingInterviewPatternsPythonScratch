import collections
import heapq
from dataclasses import dataclass
from typing import Any, List


class Heap:

    def k_most_frequent_str(self, k: int, input_strs: List[str]):
        count_times_present = collections.Counter(input_strs)
        priority_nodes = [PriorityNode(priority=v, payload=k) for k, v in count_times_present.items()]
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


@dataclass
class PriorityNode:
    priority: int
    payload: str

    def __lt__(self, other):
        if self.priority == other.priority:
            return self.payload < other.payload
        return self.priority < other.priority
