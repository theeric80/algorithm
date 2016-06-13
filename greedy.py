from operator import itemgetter

class ActivitySelection(object):
    def select(self, a):
        a = sorted(a, key=itemgetter(1))  # sort activities by its finish time

        result, k, n = [0], 0, len(a)
        for i in xrange(1, n):
            if a[i][0] >= a[k][1]:  # find the first activity in Sk to finish
                result.append(i)
                k = i
        return result

if __name__ == '__main__':
    def test_activity_selection():
        print '> test_activity_selection'
        a = [(1,4), (3,5), (0,6), (5,7), (3,9), (5,9), (6,10), (8,11), (8,12), (2,14), (12,16)]
        result = ActivitySelection().select(a)
        print 'S = {}'.format(result)

    def main():
        test_activity_selection()

    main()
