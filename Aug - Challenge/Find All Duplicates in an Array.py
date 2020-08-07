class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        res = []
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                res += [nums[i]]
        return res