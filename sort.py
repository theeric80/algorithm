import operator
from itertools import islice, ifilter, takewhile, count
from functools import partial

def less(x, y):
    return cmp(x, y) < 0

def exch(iterable, i, j):
    iterable[j], iterable[i] = iterable[i], iterable[j]

def is_sorted(iterable):
    return not any(less(iterable[i], iterable[i-1]) for i in xrange(1, len(iterable)))

def selection_sort(a):
    N = len(a)
    for i in xrange(N-1):
        _min = i
        for j in xrange(i+1, N):
            if less(a[j], a[_min]):
                _min = j
        exch(a, i, _min)

def insertion_sort(a):
    N = len(a)
    for i in xrange(1, N):
        for j in xrange(i, 0, -1):
            if not less(a[j], a[j-1]):
                break
            exch(a, j, j-1)

def bubble_sort(a):
    N = len(a)
    for i in xrange(N-1):
        for j in xrange(N-1, i, -1):
            if less(a[j], a[j-1]):
                exch(a, j, j-1)

def mergesort(a):
    def merge(a, lo, mid, hi):
        aux = a[:]
        i, j = lo, mid + 1
        for k in xrange(lo, hi+1):
            if i > mid:
                a[k] = aux[j]
                j += 1
            elif j > hi:
                a[k] = aux[i]
                i += 1
            elif less(aux[i], aux[j]):
                a[k] = aux[i]
                i += 1
            else:
                a[k] = aux[j]
                j += 1

    # Top-down
    def sort(a, lo, hi):
        if hi <= lo: return
        mid = lo + (hi-lo)/2
        sort(a, lo, mid)
        sort(a, mid+1, hi)
        merge(a, lo, mid, hi)

    # Bottom-up
    def sort_b(a):
        N = len(a)
        last = N - 1
        for sz in takewhile(lambda x:x<N, (2**i for i in count(0))):
            for lo in xrange(0, N-sz+1, sz+sz):
                mid = lo + sz - 1
                hi = min(lo + sz + sz - 1, last)
                merge(a, lo, mid, hi)

    #sort(a, 0, len(a)-1)
    sort_b(a);

def quicksort(a):
    # Hoare partition
    def partition(a, lo, hi):
        v = a[lo]
        i, j = lo-1, hi+1
        while True:
            # do-while
            while True:
                j -= 1
                if a[j] <= v: break
            # do-while
            while True:
                i += 1
                if a[i] >= v: break
            if i < j:
                exch(a, i, j)
            else:
                # a[lo, j] <= v and a[j+1, hi] >= v
                return j

    def sort(a, lo, hi):
        if hi <= lo: return
        j = partition(a, lo, hi)
        sort(a, lo, j)
        sort(a, j+1, hi)

    sort(a, 0, len(a) - 1)

def quicksort_3(a):
    # Dijkstra 3-way partitioning
    def partition(a, lo, hi):
        v = a[lo]
        lt, i, gt = lo, lo+1, hi
        while gt >= i:
            '''
            a[lo    , lt-1] < v
            a[lt    , i-1]  = v
            a[i     , gt]   not examined
            a[gt+1  , hi]   > v
            '''
            if less(a[i], v):
                exch(a, lt, i)
                lt += 1
                i += 1
            elif less(v, a[i]):
                exch(a, i, gt)
                gt -= 1
            else:
                i += 1
        return lt, gt

    def sort(a, lo, hi):
        if hi <= lo: return
        lt, gt = partition(a, lo, hi)
        sort(a, lo, lt-1)
        sort(a, gt+1, hi)

    sort(a, 0, len(a) - 1)

def heapsort(a):
    # zero-based indexing
    def parent(k):
        return (k-1) / 2

    def lchild(k):
        return 2*k + 1

    def swim(k):
        while True:
            j = parent(k)
            if j < 0 or not less(a[j], a[k]):
                break
            exch(a, k, j)
            k = j

    def sink(k, hi):
        while True:
            j = lchild(k)
            if j < hi and less(a[j], a[j+1]):
                j += 1
            if j > hi or not less(a[k], a[j]):
                break
            exch(a, k, j)
            k = j

    N = len(a)
    last = N - 1

    def heapify_swim():
        # use swim, from left to right
        for i in xrange(1, N):
            swim(i)

    def heapify_sink():
        # use sink, from right to left
        hi = (last - 1) / 2 # hi: the parent of the last node
        for i in xrange(hi, -1, -1):
            sink(i, last)

    #heapify_swim()
    heapify_sink()

    # sortdown
    for hi in xrange(last, 0, -1):
        exch(a, 0, hi)
        sink(0, hi - 1)

def counting_sort(a, R):
    N = len(a)
    count = [0 for i in xrange(R)]
    aux = a[:]

    # count[i]: the number of elements equal to i
    for i in xrange(N):
        count[a[i]] = count[a[i]] + 1

    # count[i]: the number of elements less than or equal to i
    for r in xrange(1, R):
        count[r] = count[r] + count[r-1]

    for i in xrange(N-1, -1, -1):
        j = aux[i]
        a[count[j] - 1] = j # a: zero-based indexing
        count[j] = count[j] - 1

if __name__ == '__main__':
    import random
    a = range(0, 10)
    a.extend(range(0, 10))

    for i in xrange(10):
        random.shuffle(a)
        #selection_sort(a)
        #insertion_sort(a)
        #bubble_sort(a)
        #mergesort(a)
        #quicksort(a)
        #quicksort_3(a)
        heapsort(a)
        #counting_sort(a, 10)
        assert(is_sorted(a))

    print 'sorted: {}'.format(a)
