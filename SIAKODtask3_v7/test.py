import unittest
from heap import MinHeap
from main import merge_files


class TestMinHeap(unittest.TestCase):
    def test_heapify_o_n(self):
        items = [(5, 'a'), (3, 'b'), (7, 'c'), (1, 'd'), (9, 'e')]
        heap = MinHeap(items)
        self.assertEqual(heap.pop(), (1, 'd'))
        self.assertEqual(heap.pop(), (3, 'b'))
        self.assertEqual(heap.size(), 3)

    def test_push_and_pop(self):
        heap = MinHeap()
        heap.push(5, "a")
        heap.push(3, "b")
        heap.push(7, "c")
        self.assertEqual(heap.pop(), (3, "b"))
        self.assertEqual(heap.pop(), (5, "a"))
        self.assertEqual(heap.pop(), (7, "c"))

    def test_peek(self):
        heap = MinHeap([(5, 'a'), (3, 'b')])
        self.assertEqual(heap.peek(), (3, 'b'))
        self.assertEqual(heap.size(), 2)  # peek не удаляет

    def test_replace_top(self):
        heap = MinHeap([(5, 'a'), (3, 'b')])
        old_min = heap.replace_top(4, 'd')
        self.assertEqual(old_min, (3, 'b'))
        self.assertEqual(heap.peek(), (4, 'd'))

    def test_empty_heap(self):
        heap = MinHeap()
        self.assertTrue(heap.is_empty())
        with self.assertRaises(IndexError):
            heap.pop()


class TestMergeFiles(unittest.TestCase):
    def test_empty_input(self):
        plan, cost = merge_files([])
        self.assertEqual(plan, [])
        self.assertEqual(cost, 0)

    def test_single_file(self):
        plan, cost = merge_files([100])
        self.assertEqual(plan, [])
        self.assertEqual(cost, 0)

    def test_two_files(self):
        plan, cost = merge_files([3, 5])
        self.assertEqual(len(plan), 1)
        self.assertEqual(plan[0], (0, 1, 8))
        self.assertEqual(cost, 8)

    def test_zero_sizes(self):
        plan, cost = merge_files([0, 0, 0])
        self.assertEqual(cost, 0)
        self.assertEqual(len(plan), 2)

    def test_equal_sizes_tie_breaking(self):
        sizes = [5, 5, 5]
        plan, cost = merge_files(sizes)
        self.assertEqual(plan[0], (0, 1, 10))
        self.assertEqual(plan[1], (2, 3, 15))
        self.assertEqual(cost, 25)

    def test_use_previous_result(self):
        sizes = [1, 2, 3, 4]
        plan, cost = merge_files(sizes)
        self.assertEqual(plan[0], (0, 1, 3))
        self.assertEqual(plan[1], (2, 4, 6))
        self.assertEqual(plan[2], (3, 5, 10))
        self.assertEqual(cost, 19)

    def test_four_files_example(self):
        sizes = [4, 3, 2, 6]
        plan, cost = merge_files(sizes)
        self.assertEqual(cost, 29)
        self.assertEqual(len(plan), 3)

if __name__ == "__main__":
    unittest.main()