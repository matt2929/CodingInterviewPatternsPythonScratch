class SlidingWindow:

    def find_longest_edit_with_edit(self, input_str: str, edits: int) -> int:
        frequency = [0] * 26
        left_pntr = 0
        right_pntr = 0
        while right_pntr < len(input_str):
            frequency[ord(input_str[right_pntr]) - ord('a')] += 1
            maximum_freq = max(frequency)
            if (right_pntr - left_pntr + 1) - maximum_freq > edits:
                frequency[ord(input_str[left_pntr]) - ord('a')] -= 1
                left_pntr += 1
            right_pntr += 1
        return right_pntr - left_pntr
