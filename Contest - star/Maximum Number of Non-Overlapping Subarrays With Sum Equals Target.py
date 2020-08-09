#5471. Maximum Number of Non-Overlapping Subarrays With Sum Equals Target
class Solution(object):
    def maxNonOverlapping(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        '''
        TLE o(n2)
        first solution I brute force all possible subarrays and use greedy to count the non-overlapping ones
        res = []
        def helper(ind,nums,target,res):
            tmp = 0
            for k in range(ind,len(nums)):
                tmp += nums[k]
                if tmp == target:
                    res.append([ind,k]) 
                    return
                    
        for i in range(len(nums)):
            helper(i,nums,target,res)
        res = sorted(res,key = lambda x:x[1])
        #print res
        def greedy(res):
            count = 1
            end = res[0][1]
            for pair in res:
                start = pair[0]
                if start > end:
                    count += 1
                    end = pair[1]
            return count
        if len(res)<=1:
            return len(res)
        else:
            return greedy(res)'''

        #print(res)
        # prefix sum O(n) with greedy 
        res = 0
        sum = 0
        seen = set()
        seen.add(0)
        for k in nums:
            sum += k
            if sum - target in seen:
                res += 1
                seen = set() # greedy, once find, new the set
            seen.add(sum)
        return res