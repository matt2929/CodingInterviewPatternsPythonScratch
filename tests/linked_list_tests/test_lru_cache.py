import unittest

from linked_lists.lru_cache import LRUCache


class TestLRUCache(unittest.TestCase):

    def test_lru_cache(self):
        lru_cache = LRUCache(2)
        for i in range(3):
            for j in reversed(range(4)):
                lru_cache.put(j, i)

        lru_cache.print_what_look_like()