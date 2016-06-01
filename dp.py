
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

class LCSLength(object):
    def lcs_length(self, X, Y):
        X, Y = [0]+X, [0]+Y
        m, n = len(X), len(Y)
        c = [[0] * n for i in xrange(m)]
        for i in xrange(1, m):
            for j in xrange(1, n):
                if X[i] == Y[j]:
                    c[i][j] = c[i-1][j-1] + 1
                elif X[i] != Y[j]:
                    c[i][j] = max(c[i-1][j], c[i][j-1])
        return c[-1][-1]

if __name__ == '__main__':
    def test_cut_rod():
        print '> test_cut_rod'

        a = CutRod()
        p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
        for n in xrange(1, 11):
            r = a.cut(p, n)
            print 'r{} = {}'.format(n, r)

    def test_lcs_length():
        a = LCSLength()
        X = ['A', 'B', 'C', 'B', 'D', 'A', 'B']
        Y = ['B', 'D', 'C', 'A', 'B', 'A']
        q = a.lcs_length(X, Y)
        print 'LCS length = {}'.format(q)

    def main():
        #test_cut_rod()
        test_lcs_length()

    main()
