import unittest

from linked_lists.sliding_window_edits import SlidingWindow


class SlidingWindowTests(unittest.TestCase):

    def test_find_longest_edit_with_edit(self):
        window = SlidingWindow()
        assert window.find_longest_edit_with_edit("aabcdcca", 2) == 5
        assert window.find_longest_edit_with_edit("abcd", 2) == 3
        assert window.find_longest_edit_with_edit("abcd", 1) == 2
        assert window.find_longest_edit_with_edit("abcd", 0) == 1
        assert window.find_longest_edit_with_edit("aaa", 0) == 3
