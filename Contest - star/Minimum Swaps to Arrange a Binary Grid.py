# 5477. Minimum Swaps to Arrange a Binary Grid
class Solution(object):
    def minSwaps(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # bubble sort
        n = len(grid)
        def count(a):
            count = 0
            for i in range(n-1,-1,-1):
                if a[i] == 0:
                    count += 1
                else:
                    return count
            return count
        arr = [count(grid[i]) for i in range(n)]
        print(arr) # count how many zeros in each line, target is [5,4,3,2,1,0] when n = 6
        
        res = 0
        for i in range(n):
            target = n - i - 1 # decreasing order, no need to consider mis-match
            cur = arr[i]
            if cur >= target:
                continue
            flag = False
            for j in range(i + 1, n):
                if arr[j] >= target:
                    flag = True
                    res += j - i
                    arr[i+1:j+1] = arr[i:j] # shift lines, cur line is moved to next line no need to actually change the value of cur line
                    break
            if not flag:
                return -1
        return res