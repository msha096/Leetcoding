class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        '''
        # Brute Force TLE
        for i in range(len(nums)-1):
            for j in range(i+1,min(i+k+1,len(nums))):
                #print nums[i],nums[j]
                if abs(nums[j] - nums[i])<=t:
                    return True
        return False'''
        
        # Bucket sort
        if t < 0: return False
        n = len(nums)
        d = {}
        w = t + 1
        for i in xrange(n):
            m = nums[i] / w #int type because of python 2version
            #print m
            if m in d:
                return True
            if m - 1 in d and abs(nums[i] - d[m - 1]) < w:
                return True
            if m + 1 in d and abs(nums[i] - d[m + 1]) < w:
                return True
            d[m] = nums[i]
            if i >= k: del d[nums[i - k] / w]
        return False