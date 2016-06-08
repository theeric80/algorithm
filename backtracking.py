
class Permutation(object):
    def permute(self, nums, used, stack):
        if len(nums) == len(stack):
            print stack
            return

        for i, x in enumerate(nums):
            if not used[i]:
                used[i] = True
                stack.append(x)
                self.permute(nums, used, stack)
                stack.pop()
                used[i] = False

class Combination(object):
    def combine(self, nums, start, stack):
        print stack

        n = len(nums)
        for i in xrange(start, n):
            stack.append(nums[i])
            self.combine(nums, i+1, stack)
            stack.pop()

class EightQueensPuzzle(object):
    def solution(self, n):
        queens = []
        self.solve(n, 0, queens)

    def valid(self, queens, row, col):
        for r, c in queens:
            if row == r:           return False  # check row
            if col == c:           return False  # check column
            if (row-r) == (col-c): return False  # check upper-left diagonal
            if (r-row) == (col-c): return False  # check lower-left diagonal
        return True

    # http://www.geeksforgeeks.org/backtracking-set-3-n-queen-problem/
    def solve(self, n, col, queens):
        if col >= n:
            print queens
            return True

        for i in xrange(n):
            if self.valid(queens, i, col):
                queens.append((i, col))           # place this queen in board[i][col]
                if self.solve(n, col+1, queens):  # place rest of the queens
                    return True
                queens.pop()                      # BACKTRACK

if __name__ == '__main__':
    def test_permute():
        print '> test_permute'
        nums = range(4)
        n = len(nums)
        used = [False] * n
        Permutation().permute(nums, used, [])

    def test_combine():
        print '> test_combine'
        nums = range(4)
        Combination().combine(nums, 0, [])

    def test_eight_queen_puzzle():
        print '> test_eight_queen_puzzle'
        n = 8
        EightQueensPuzzle().solution(n)

    def main():
        #test_permute()
        #test_combine()
        test_eight_queen_puzzle()

    main()
