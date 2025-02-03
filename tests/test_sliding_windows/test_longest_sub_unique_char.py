import unittest

from linked_lists.longest_sub_unique_char import LongestUniqueSubstring


class LongestUniqueSubstringTests(unittest.TestCase):

    def test_longest_unique_substr(self) -> int:
        luss = LongestUniqueSubstring()
        assert luss.longest_unique_substr("abcd") == 4
        assert luss.longest_unique_substr("abcdb") == 4
        assert luss.longest_unique_substr("abcdabc") == 4
        assert luss.longest_unique_substr("abababababababababab") == 2
        assert luss.longest_unique_substr("abcdefghidefg") == 9
