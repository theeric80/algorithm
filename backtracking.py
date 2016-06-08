
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

    def main():
        test_permute()
        test_combine()

    main()
