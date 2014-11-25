import collections

class Stack(collections.Iterable):
    def __init__(self):
        self._first = None

    def push(self, item):
        # Insert at the beginning
        node = self.Node()
        node._item = item
        node._next = self._first
        self._first = node

    def pop(self):
        # Remove from the beginning
        node = self._first
        self._first = self._first._next
        return node._item

    def is_empty(self):
        return self._first is None

    def __iter__(self):
        # Implement iteration with generator
        current = self._first
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

class BST(ST):
    def __init__(self):
        self._root = None

    def get(self, key):
        return self._get(self._root, key)

    def put(self, key, val):
        self._root = self._put(self._root, key, val)

    def size(self):
        return self._size(self._root)

    def delete(self, key):
        pass

    def keys(self):
        # Implement iteration with generator
        # Depth-First Search, In-Order
        stack = Stack()
        current = self._root
        while not stack.is_empty() or current:
            if current is not None:
                stack.push(current)
                current = current._left
            else:
                current = stack.pop()
                yield current._val
                current = current._right

    def _get(self, x, key):
        if x is None:       return None
        if   key < x._key:  return self._get(x._left, key)
        elif key > x._key:  return self._get(x._right, key)
        else:               return x._val

    def _put(self, x, key, val):
        if x is None:       return self.Node(key, val, 1)
        if   key < x._key:  x._left  = self._put(x._left, key, val)
        elif key > x._key:  x._right = self._put(x._right, key, val)
        else:               x._val = val

        x._N = self._size(x._left) + self._size(x._right) + 1
        return x

    def _size(self, x):
        return 0 if x is None else x._N

    class Node(object):
        def __init__(self, key, val, N):
            self._key = key
            self._val = val
            self._N = N
            self._left = None
            self._right = None

if __name__ == '__main__':
    pass
