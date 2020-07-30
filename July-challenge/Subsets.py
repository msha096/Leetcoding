class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        '''
        Input: nums = [1,2,3]
        Output:
        [
        [3],
        [1],
        [2],
        [1,2,3],
        [1,3],
        [2,3],
        [1,2],
        []
        ]
        '''
        output = [[]]
        for num in nums:
            #print(num)
            output += [cur + [num] for cur in output]
            #print(output)
        return output