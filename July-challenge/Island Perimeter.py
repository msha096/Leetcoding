class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # step 1: create a n+1 * n+1 grid, with the outside layer set as water
        m = len(grid)
        if m==0:
            return 0
        n = len(grid[0])
        
        for i in range(m):
            grid[i].insert(0,0)
            grid[i].append(0)
            
        grid.insert(0, [0] * (n + 2))
        grid.append([0] * (n + 2))
        #print(grid)
        
        # step 2: dp, to right and down side, when different: add 1 (side) to the count
        count = 0
        for i in range(m + 1):
            for j in range(n + 1):
                if grid[i][j] != grid[i+1][j]:
                    count += 1
                if grid[i][j] !=g rid[i][j+1]:
                    count += 1
        return count