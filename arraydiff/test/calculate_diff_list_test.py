import unittest

from arraydiff.array_diff.array_diff import calculate_difference_list


class Test_test(unittest.TestCase):

    def test_sample(self):
        list_a = [1,3,5,6,8,9]
        list_b = [1,2,5,7,9]
        diff = calculate_difference_list(list_a, list_b)
        self.assertListEqual(sorted(diff['additions']), [2,7])
        self.assertListEqual(sorted(diff['deletions']), [3,6,8])

    def test_sample_invert_target_current(self):
        list_a = [1,2,5,7,9]
        list_b = [1,3,5,6,8,9]
        diff = calculate_difference_list(list_a, list_b)
        self.assertListEqual(sorted(diff['additions']), [3,6,8])
        self.assertListEqual(sorted(diff['deletions']), [2,7])

    def test_all_deletes(self):
        list_a = [1, 3, 5, 6, 8, 9]
        list_b = []
        diff = calculate_difference_list(list_a, list_b)
        self.assertListEqual(sorted(diff['additions']), [])
        self.assertListEqual(sorted(diff['deletions']), [1, 3, 5, 6, 8, 9])

    def test_all_adds(self):
        list_a = []
        list_b = [1, 1, 1, 1, 1, 2]
        diff = calculate_difference_list(list_a, list_b)
        self.assertListEqual(sorted(diff['additions']), [1, 1, 1, 1, 1, 2])
        self.assertListEqual(sorted(diff['deletions']), [])

    def test_no_adds_no_dels(self):
        list_a = [1,2,3]
        list_b = [1,2,3]
        diff = calculate_difference_list(list_a,list_b)
        self.assertListEqual(sorted(diff['additions']), [])
        self.assertListEqual(sorted(diff['deletions']), [])

    def test_no_adds(self):
        list_a = [1,2,3,4]
        list_b = [1,2,3]
        diff = calculate_difference_list(list_a,list_b)
        self.assertListEqual(sorted(diff['additions']), [])
        self.assertListEqual(sorted(diff['deletions']), [4])

    def test_no_dels(self):
        list_a = [1,2,3]
        list_b = [1,2,3, 4]
        diff = calculate_difference_list(list_a,list_b)
        self.assertListEqual(sorted(diff['additions']), [4])
        self.assertListEqual(sorted(diff['deletions']), [])

    def test_dels_and_adds_1(self):
        list_a = [1,2,3,4,6]
        list_b = [1,2,3,5]
        diff = calculate_difference_list(list_a,list_b)
        self.assertListEqual(sorted(diff['additions']), [5])
        self.assertListEqual(sorted(diff['deletions']), [4,6])

    def test_dels_and_adds_2(self):
        list_a = [1,2,3,5]
        list_b = [1,2,3,4,6]
        diff = calculate_difference_list(list_a,list_b)
        self.assertListEqual(sorted(diff['additions']), [4,6])
        self.assertListEqual(sorted(diff['deletions']), [5])

    def test_empty_lists(self):
        list_a = []
        list_b = []
        diff = calculate_difference_list(list_a, list_b)
        self.assertListEqual(sorted(diff['additions']), [])
        self.assertListEqual(sorted(diff['deletions']), [])


if __name__ == '__main__':
    unittest.main()
