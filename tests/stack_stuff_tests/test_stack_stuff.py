import unittest

from parameterized import parameterized

from stacks.stack_stuff import StackStuff


class StackStuffTests(unittest.TestCase):

    @parameterized.expand([
        ([2, 6, 3, 8], [8, 3, 6, 2]),
    ])
    def test_reverse_list(self, input, expected):
        ss = StackStuff()
        assert ss.reverse_list_via_stack(input) == expected

    @parameterized.expand([
        ("{[(())]}", True),
        ("{}", True),

        ("()" * 100000, True),
        ("(" * 100000 + ")" * 100000, True),
        ("(" * 100000 + ")" * 10, False),
    ])
    def test_valid_paren(self, test_case, expected):
        ss = StackStuff()
        assert ss.is_valid_parenthesis(test_case) == expected

    @parameterized.expand([
        ([5, 2, 4, 6, 1], [6, 4, 6, -1, -1]),
        ([1, 2, 3, 4, 5, 6], [2, 3, 4, 5, 6, -1]),
        ([1, 1, 1, 1, 1, 1, 1, 1], [-1, -1, -1, -1, -1, -1, -1, -1]),
        ([1, 30, 40, 2, 10, 9, 1, 7, 8], [30, 40, -1, 10, -1, -1, 7, 8, -1]),
        ([1, 1, 1, 1, 1, 1, 1, 1, 2], [2, 2, 2, 2, 2, 2, 2, 2, -1]),
    ])
    def test_valid_paren(self, test_case, expected):
        ss = StackStuff()
        assert ss.find_first_bigger_right(test_case) == expected

    @parameterized.expand([
        ('a', False),
        ('0', True),
        ('1', True),
        ('2', True),
        ('3', True),
        ('4', True),
        ('5', True),
        ('6', True),
        ('7', True),
        ('8', True),
        ('9', True),
        ('7E', False),
        ('ß', False),
    ])
    def test_is_char_digit(self, input_char, expected):
        ss = StackStuff()
        assert ss.__is_char_digit__(input_char) == expected

    @parameterized.expand([
        ('(123+2)-(33+4)', 88),

    ])
    def test_is_char_digit(self, input_char, expected):
        ss = StackStuff()
        assert ss.tokenize_input_str(input_char) == expected

