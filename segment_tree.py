import math

class SegmentTree(object):
    def __init__(self, a):
        n = len(a)
        sz = self._tree_size(n)

        self._n = n
        self._sum = [0] * sz
        self._build(a, 0, n-1, 1)

    def _tree_size(self, n):
        """
        2^x = n => x = ceil(log(n, 2))
        h = x + 1
        sz = 2^h - 1
        """
        h = int(math.ceil(math.log(n, 2))) + 1
        return pow(2,h) - 1

    def _build(self, a, lo, hi, i):
        if lo == hi:
            self._sum[i] = a[lo]
            return

        mid = lo + (hi-lo)/2
        l, r = 2*i, 2*i+1

        self._build(a, lo, mid, l)
        self._build(a, mid+1, hi, r)

        self._sum[i] = self._sum[l] + self._sum[r]

    def _update(self, k, val, lo, hi, i):
        if lo == hi:
            self._sum[i] = val
            return

        mid = lo + (hi-lo)/2
        l, r = 2*i, 2*i+1

        if k <= mid:
            self._update(k, val, lo, mid, l)
        if k > mid:
            self._update(k, val, mid+1, hi, r)

        self._sum[i] = self._sum[l] + self._sum[r]

    def update(self, k, val):
        lo, hi = 0, self._n-1
        self._update(k, val, lo, hi, 1)

    def _range_sum(self, l, r, lo, hi, i):
        if l <= lo and r >= hi:
            return self._sum[i]

        mid = lo + (hi-lo)/2

        result = 0
        if l <= mid:
            result += self._range_sum(l, r, lo, mid, 2*i)
        if r > mid:
            result += self._range_sum(l, r, mid+1, hi, 2*i+1)
        return result

    def range_sum(self, l, r):
        lo, hi = 0, self._n-1
        return self._range_sum(l, r, lo, hi, 1)

def main():
    a = [1,3,5,7,9,11]
    t = SegmentTree(a)
    print 'seq = {}'.format(a)

    inputs = [(0,2), (1,3),(3,5)]
    for l, r in inputs:
        print '({}, {}) = {}'.format(l, r, t.range_sum(l,r))


    k, val = 2, 12
    t.update(k, val)
    print 'update: a[{}] = {}'.format(k, val)

    a[k] = val
    print 'seq = {}'.format(a)

    for l, r in inputs:
        print '({}, {}) = {}'.format(l, r, t.range_sum(l,r))

if __name__ == '__main__':
   main() 
