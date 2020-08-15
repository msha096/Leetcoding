class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        l = len(intervals) # total num of intervals
        
        if l <= 1:
            return 0
        
        intervals.sort( key = lambda end:end[1]) # sort according to the end
        
        # greedy algo, find the number of non-overlapping intervals, then substract
        
        k = 1 # num of non-overlapping 
        end = intervals[0][1]
        
        for i in range(1,l):
            if intervals[i][0] >= end:
                k += 1
                end = intervals[i][1]
                
        return l - k