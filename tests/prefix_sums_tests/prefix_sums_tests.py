import unittest
from parameterized import parameterized
from prefix_sums.prefix_sums import PREFIX_SUMS

class PREFIX_SUMSTests(unittest.TestCase):


  @parameterized.expand([
        ('a', False),
        ('b', False),
    ])
  def test_prefix_sums(self, input, expected):
      prefix_sums = PREFIX_SUMS()
