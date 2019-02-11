class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #_keys = range(min(nums), max(nums))
        length = len(nums)
        correct = set()
        for i1 in range(length):
            for i2 in range(i1, length):
                for i3 in range(i2, length):
                    n = (nums[i1], nums[i2], nums[i3])
                    if sum(n) == 0:
                        correct.add(tuple(sorted(n)))
        return [list(c) for c in correct]


s = Solution()
s.threeSum(nums = [-1, 0, 1, 2, -1, -4])
