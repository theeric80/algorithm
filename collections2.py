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

if __name__ == '__main__':
    pass
