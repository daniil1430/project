class MinHeap:

    def __init__(self, items = None):
        self._data = []
        if items:
            self.heapify(items)

    def size(self):
        return len(self._data)

    def is_empty(self):
        return self.size() == 0

    def peek(self):
        if self.is_empty():
            raise IndexError("Куча пуста")
        return self._data[0]

    def _parent(self, i):
        return (i - 1) // 2

    def _left(self, i):
        return 2 * i + 1

    def _right(self, i):
        return 2 * i + 2

    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _sift_up(self, i):
        while i > 0:
            parent = self._parent(i)
            if self._data[i] < self._data[parent]:
                self._swap(i, parent)
                i = parent
            else:
                break

    def _sift_down(self, i):
        n = self.size()
        while True:
            smallest = i
            left = self._left(i)
            right = self._right(i)

            if left < n and self._data[left] < self._data[smallest]:
                smallest = left
            if right < n and self._data[right] < self._data[smallest]:
                smallest = right

            if smallest != i:
                self._swap(i, smallest)
                i = smallest
            else:
                break

    def push(self, key, value):
        self._data.append((key, value))
        self._sift_up(self.size() - 1)

    def pop(self):
        if self.is_empty():
            raise IndexError("Куча пуста")
        if self.size() == 1:
            return self._data.pop()

        min_item = self._data[0]
        self._data[0] = self._data.pop()
        self._sift_down(0)
        return min_item

    def replace_top(self, key, value):
        if self.is_empty():
            raise IndexError("Куча пуста")
        min_item = self._data[0]
        self._data[0] = (key, value)
        self._sift_down(0)
        return min_item

    def heapify(self, items):
        self._data = items[:]
        for i in range(self.size() // 2 - 1, -1, -1):
            self._sift_down(i)