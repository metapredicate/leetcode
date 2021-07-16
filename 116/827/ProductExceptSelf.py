from functools import reduce
from operator import mul

class Solution:
    def productExceptSelf(self, nums):
        result = nums[:]
        for index, _ in enumerate(nums):
            temp = nums[:]
            temp.pop(index)
            result[index] = reduce(mul, temp, 1)
        return result

if __name__ == '__main__':
    foo = Solution()
    print(foo.productExceptSelf([1,2,3,4,5]))
