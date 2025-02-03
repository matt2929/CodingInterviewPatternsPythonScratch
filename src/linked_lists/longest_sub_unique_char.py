class LongestUniqueSubstring:

    def longest_unique_substr(self, input_str: str) -> int:
        pointer = 0
        current_left = 0
        unique_char_map = {}
        biggest = -1
        while pointer < len(input_str):
            if input_str[pointer] in unique_char_map and unique_char_map[input_str[pointer]] >= current_left:
                current_left = pointer
            biggest = max((pointer - current_left)+1, biggest)
            unique_char_map[input_str[pointer]] = pointer
            pointer += 1
        print(f"{input_str} biggest = {biggest}")
        return biggest
