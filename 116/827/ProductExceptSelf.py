from functools import reduce
from operator import mul

class Solution:
    def productExceptSelf(self, nums):
        memo = {}
        result = []
        for index, value in enumerate(nums):
            if (value not in memo):
                temp = nums.pop(index)
                memo[value] = reduce(mul, nums, 1)
                nums.insert(index, value)
            result.append(memo[value])
        return result

if __name__ == '__main__':
    foo = Solution()
    print(foo.productExceptSelf([1,2,3,4,5]))
