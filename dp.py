
class CutRod(object):
    def cut(self, p, n):
        #return self.cut_rod(p, n)

        #r = [-1] * (n+1)
        #return self.memoized_cut_rod(p, n, r)

        return self.bottom_up_cut_rod(p, n)

    def cut_rod(self, p, n):
        if n == 0:
            return 0

        q = max(p[i] + self.cut_rod(p, n-i) for i in xrange(1, n+1))
        return q

    def memoized_cut_rod(self, p, n, r):
        if r[n] >= 0:
            return r[n]

        if n == 0:
            return 0

        q = max(p[i] + self.memoized_cut_rod(p, n-i, r) for i in xrange(1, n+1))
        r[n] = q
        return q

    def bottom_up_cut_rod(self, p, n):
        r = [0] * (n+1)
        for j in xrange(1, n+1):
            q = max(p[i] + r[j-i] for i in xrange(1, j+1))
            r[j] = q
        return r[n]

if __name__ == '__main__':
    def test_cut_rod():
        print '> test_cut_rod'

        a = CutRod()
        p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
        for n in xrange(1, 11):
            r = a.cut(p, n)
            print 'r{} = {}'.format(n, r)

    def main():
        test_cut_rod()

    main()
