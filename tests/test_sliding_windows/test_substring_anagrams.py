import unittest
from collections import defaultdict

from sliding_windows.substring_anagrams import SubstringAnagrams


class SubstringAnagramsTests(unittest.TestCase):

    def test_number_of_anagram_substrings(self):
        anagrams = SubstringAnagrams()
        actual = anagrams.number_of_anagram_substrings("abccba", "bc")
        assert actual == 2, f"actual: {actual}"
