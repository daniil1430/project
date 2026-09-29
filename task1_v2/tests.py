import unittest
from main import max_subarray_v1
from main import max_subarray_v2
from main import max_subarray_v3


class TestMaxSubarray(unittest.TestCase):
    def test1(self):
        arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        self.assertEqual(max_subarray_v1(arr), 6)
        self.assertEqual(max_subarray_v2(arr), 6)
        self.assertEqual(max_subarray_v3(arr), 6)

    def test2(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(max_subarray_v1(arr), 15)
        self.assertEqual(max_subarray_v2(arr), 15)
        self.assertEqual(max_subarray_v3(arr), 15)

    def test3(self):
        arr = [-3, -5, -1, -8]
        self.assertEqual(max_subarray_v1(arr), -1)
        self.assertEqual(max_subarray_v2(arr), -1)
        self.assertEqual(max_subarray_v3(arr), -1)

    def test4(self):
        self.assertEqual(max_subarray_v1([42]), 42)
        self.assertEqual(max_subarray_v2([42]), 42)
        self.assertEqual(max_subarray_v3([42]), 42)

    def test5(self):
        self.assertEqual(max_subarray_v1([]), 0)
        self.assertEqual(max_subarray_v2([]), 0)
        self.assertEqual(max_subarray_v3([]), 0)

    def test6(self):
        arr = [0, 0, 0]
        self.assertEqual(max_subarray_v1(arr), 0)
        self.assertEqual(max_subarray_v2(arr), 0)
        self.assertEqual(max_subarray_v3(arr), 0)


if __name__ == '__main__':
    unittest.main()