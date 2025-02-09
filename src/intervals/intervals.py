from typing import Tuple, List


class INTERVALS:

    def do_intervals_overlap(self, interval_a: Tuple[int, int], interval_b: Tuple[int, int]):
        return not (interval_a[1] < interval_b[0] or interval_b[1] < interval_a[0])

    def merge_overlapping_intervals(self, input_intervals: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        if not input_intervals:
            return []
        output = []
        temp_interval = None
        input_intervals.sort(key=lambda x: x[0])
        for i in input_intervals:
            if not temp_interval:
                temp_interval = i
            elif self.do_intervals_overlap(temp_interval, i):
                temp_interval = (temp_interval[0], max(i[1], temp_interval[1]))
            else:
                output.append(temp_interval)
                temp_interval = i
        if temp_interval:
            output.append(temp_interval)
        return output
