class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        n = len(intervals)
        for i in range(n):
            intervals[i].append(i)
        intervals.sort(key = lambda x:x[0])
        #print intervals
        res = [-1 for i in range(n)]
        
        def binarySearch(intervals,end):
            left = 0
            right = len(intervals) -1
            while left <= right:
                mid =  (left+ right) // 2
                if intervals[mid][0] >= end and (mid == 0 or intervals[mid-1][0] < end):
                    return intervals[mid][2]
                elif intervals[mid][0] < end:
                    left = mid + 1
                elif intervals[mid][0] >= end and (mid != 0 or intervals[mid-1][0] >= end):
                    right = mid - 1
            return -1
        for i in range(n):
            ind =  binarySearch(intervals,intervals[i][1]) 
            if ind != -1:
                res[intervals[i][2]] = ind
        return res