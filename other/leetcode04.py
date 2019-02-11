class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        for i in range(length):
            m = (target - nums.pop())
            if m in nums:
                return [nums.index(m), length-i-1]

s = Solution()
print(s.twoSum(nums = [2, 7, 11, 15], target = 9))
