def find_missing(l1,l2):
    if l1 == [] and l2 == []:
        return 0
    elif l1 == l2:
        return 0
    s1 = set(l1)
    s2 = set(l2)
    for i in (s1^s2):
        print i,

import unittest
class MissingNumberTest(unittest.TestCase):
    """docstring for MissingNumberTest"""

    def test_empty_list(self):
        self.assertEqual(0, find_missing([], []),
                         msg='should return 0 for empty list')

    def test_same_entries(self):
        list1 = find_missing([2], [2])
        list2 = find_missing([4], [4])
        list3 = find_missing([7], [7])
        self.assertEqual([0, 0, 0],
                             [list1, list2, list3],
                             msg='should return 0 for lists with the same entries')

    def test_missing_entries(self):
        list1 = find_missing([1, 2], [1, 2, 5])
        list2 = find_missing([4, 6, 8], [4, 6, 8, 10])
        list3 = find_missing([5, 4, 7, 6, 11, 66], [5, 4, 1, 7, 6, 11, 66])
        self.assertEqual([5, 10, 1],
                             [list1, list2, list3],
                             msg='should return the missing number for lists with similar entries and a missing number')
if __name__ == '__main__':
    unittest.main()