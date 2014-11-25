import collections

class Stack(collections.Iterable):
    def __init__(self):
        self.first = None

    def push(self, item):
        # Insert at the beginning
        node = self.Node()
        node._item = item
        node._next = self.first
        self.first = node

    def pop(self):
        # Remove from the beginning
        node = self.first
        self.first = self.first._next
        return node._item

    def __iter__(self):
        # Implement iteration with generator
        current = self.first
        while current is not None:
            yield current._item
            current = current._next

    class Node(object):
        def __init__(self):
            self._item = None
            self._next = None

class ST(object):
    def get(self, key):
        return None

    def put(self, key, val):
        pass

    def size(self):
        return 0

    def delete(self, key):
        self.put(key, None)

    def contains(self, key):
        return self.get(key) is not None

    def is_empty(self):
        return self.size() <= 0

    def keys(self):
        return None

class BinarySearchST(ST):
    def __init__(self):
        self._keys = []
        self._vals = []

    def get(self, key):
        i = self.rank(key)
        if i < self.size() and self._keys[i] == key:
            return self._vals[i]

        return None

    def put(self, key, val):
        i = self.rank(key)
        if i < self.size() and self._keys[i] == key:
            self._vals[i] = val
            return

        self._keys.insert(i, key)
        self._vals.insert(i, val)

    def size(self):
        return len(self._keys)

    def delete(self, key):
        i = self.rank(key)
        if i < self.size() and self._keys[i] == key:
            self._keys.pop(i)
            self._vals.pop(i)

    def keys(self):
        return self._keys

    def rank(self, key):
        # Binary search
        lo, hi = 0, len(self._keys) - 1
        while lo <= hi:
            mid = (lo + hi) / 2
            if key < self._keys[mid]:
                hi = mid - 1
            elif key > self._keys[mid]:
                lo = mid + 1
            else:
                return mid
        return lo

if __name__ == '__main__':
    pass
