from collections import Counter

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        elem_counter = Counter()
        for element in nums:
            elem_counter[element] += 1
        return [k for k, v in elem_counter.items() if v >= 2]


if __name__ == '__main__':
    foo = Solution()
    print(foo.findDuplicates([4,3,2,7,8,2,3,1]))
