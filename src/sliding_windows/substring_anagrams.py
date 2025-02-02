from collections import defaultdict


class SubstringAnagrams:

    def number_of_anagram_substrings(self, input_str: str, t: str) -> int:
        t_char_track, window_char_track = [0]*26, [0]*26
        total_anagrams = 0
        for c in t:
            t_char_track[ord(c)-ord('a')] += 1
        if len(input_str) < len(t):
            return 0
        left_pointer = 0
        right_pointer = 0
        while right_pointer < len(input_str):
            window_char_track[ord(input_str[right_pointer]) - ord('a')] += 1
            if (right_pointer-left_pointer)+1 == len(t):
                print(f"{window_char_track}\n{t_char_track}\n---")
                if window_char_track == t_char_track:
                    total_anagrams += 1
                window_left_char_index = ord(input_str[left_pointer])-ord('a')
                window_char_track[window_left_char_index] -= 1
                left_pointer += 1
            right_pointer += 1

        return total_anagrams
