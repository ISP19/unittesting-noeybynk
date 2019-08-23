import unittest
from listutil import unique

class ListUtilTest(unittest.TestCase):

    def test_single_item_list(self):
        self.assertListEqual(['hi'], unique(['hi']))
    def test_repeat_two_items_list(self):
        self.assertListEqual(['b', 'a'], unique(['b','a','a','b','b','b','a','a']))
    def test_many_items(self):
        self.assertListEqual(['N', 'n', 'o', 'e', 'y'], unique(['N','n','o','e','N','y']))
    def test_emtry_list(self):
        self.assertListEqual([], unique([]))
    def test_repeat_many_items_list(self):
        self.assertListEqual([1], unique([1,1,1,1,1]))
    def test_list_in_list_and_num(self):
        self.assertListEqual([1, [1, 2], 3], unique([1,[1,2],3,[1,2]]))
    def test_diftype(self):
        self.assertListEqual([1, 'a', '3'], unique([1, 'a', '3']))
    def test_assertion_error(self):
        with self.assertRaises(AssertionError):
            unique((1, 'a', '3'))


if __name__ == '__main__':
    unittest.main()