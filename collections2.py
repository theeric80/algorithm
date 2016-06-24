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

    def top(self):
        return self._first._item

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

    def floor(self, key):
        return None

    def ceiling(self, key):
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

    def floor(self, key):
        node = self._floor(self._root, key)
        return node._key if node is not None else None

    def ceiling(self, key):
        node = self._ceiling(self._root, key)
        return node._key if node is not None else None

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

    def _put_non_recursive(self, key, val):
        if self._root is None:
            self._root = self.Node(key, val, 1)
            return

        stack = Stack()
        x = self._root
        while True:
            if x is None:
                x = self.Node(key, val, 1)
                parent = stack.top()
                if key > parent._key: parent._right = x
                else:                 parent._left = x
                break
            elif key < x._key:
                stack.push(x)
                x = x._left
            elif key > x._key:
                stack.push(x)
                x = x._right
            else:
                x._val = val
                break

        # update nodes on search path
        for x in stack:
            x._N = self._size(x._left) + self._size(x._right) + 1

    def _floor(self, x, key):
        if x is None:       return None
        if   key == x._key: return x
        elif key < x._key:  return self._floor(x._left, key)
        t = self._floor(x._right, key)  # key > x._key
        return t if t is not None else x

    def _ceiling(self, x, key):
        if x is None:       return None
        if   key == x._key: return x
        elif key > x._key:  return self._ceiling(x._right, key)
        t = self._ceiling(x._left, key)  # key < x._key
        return t if t is not None else x

    def _size(self, x):
        return 0 if x is None else x._N

    class Node(object):
        def __init__(self, key, val, N):
            self._key = key
            self._val = val
            self._N = N
            self._left = None
            self._right = None

class RedBlackBST(BST):
    def __init__(self):
        super(RedBlackBST, self).__init__()

    def put(self, key, val):
        self._root = self._put(self._root, key, val)
        self._root._color = self.BLACK # keep the root BLACK

    def _put(self, h, key, val):
        if h is None:       return self.Node(key, val, 1, self.RED)
        if   key < h._key:  h._left  = self._put(h._left, key, val)
        elif key > h._key:  h._right = self._put(h._right, key, val)
        else:               h._val = val

        # local transformation
        if self._is_red(h._right) and not self._is_red(h._left):    h = self._rotate_left(h)
        if self._is_red(h._left)  and self._is_red(h._left._left):  h = self._rotate_right(h)
        if self._is_red(h._left)  and self._is_red(h._right):       self._flip_colors(h)

        h._N = self._size(h._left) + self._size(h._right) + 1
        return h

    def _is_red(self, h):
        return bool(h is not None) and h._color == self.RED

    def _rotate_left(self, h):
        x = h._right
        h._right = x._left
        x._left  = h

        x._color = h._color # preserve the color in the parent
        h._color = self.RED

        x._N = h._N
        h._N = self._size(h._left) + self._size(h._right) + 1
        return x

    def _rotate_right(self, h):
        x = h._left
        h._left  = x._right
        x._right = h

        x._color = h._color # preserve the color in the parent
        h._color = self.RED

        x._N = h._N
        h._N = self._size(h._left) + self._size(h._right) + 1
        return x

    def _flip_colors(self, h):
        h._color = self.RED
        h._left._color  = self.BLACK
        h._right._color = self.BLACK

    RED = True
    BLACK = False
    class Node(BST.Node):
        def __init__(self, key, val, N, color):
            super(RedBlackBST.Node, self).__init__(key, val, N)
            self._color = color

def _test_BST():
    t = BST()
    t.put(3, 3)
    t.put(1, 1)
    t.put(5, 5)
    print '--- test_BST'
    print 'keys() = {}'.format(list(t.keys()))
    keys = [0,1,2,3,4,5,6]
    for key in keys:
        print 'get({}) = {}'.format(key, t.get(key))
    for key in keys:
        print 'floor({}) = {}'.format(key, t.floor(key))
    for key in keys:
        print 'ceiling({}) = {}'.format(key, t.ceiling(key))
    print '--- test_BST end'

def main():
    _test_BST()

if __name__ == '__main__':
    main()
