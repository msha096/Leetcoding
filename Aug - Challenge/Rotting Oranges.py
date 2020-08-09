class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # BFS
        row = len(grid)
        col = len(grid[0])
        fresh = 0
        queue = []
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i,j))
        
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        if fresh == 0:
            return 0
        day = 0
        while queue:
            day += 1
            for i in range(len(queue)):
                x, y = queue.pop(0)
                for dx,dy in dirs:
                    if 0 <= x + dx < row and 0 <= y+dy < col and grid[x+dx][y+dy] == 1:
                        fresh -= 1
                        grid[x+dx][y+dy] = 2
                        queue.append((x+dx,y+dy))
                        if fresh == 0:
                            return day
        if fresh != 0:
            return -1


# the following is my first solution, these two solution has the similar speed, but the upper one is more clear.
'''
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        queue = []
        row = len(grid)
        col = len(grid[0])
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    queue.append((i,j))
                    
        def check(row,col, grid):
            for i in range(row):
                for j in range(col):
                    if grid[i][j] == 1:
                        return False
            return True
        if check(row,col,grid):
            return 0
        else:
            if len(queue) == 0:
                return -1
            
        day = 0
        while queue:
            size = len(queue)
            flag = False
            for i in range(size): # each day has 'size' rotten oranges
                x, y = queue.pop(0)
                if grid[max(x-1,0)][y] == 1:
                    grid[max(x-1,0)][y] = 2
                    flag = True
                    queue.append((max(x-1,0),y))
                if grid[x][max(y-1,0)] == 1:
                    grid[x][max(y-1,0)] = 2
                    flag = True
                    queue.append((x,max(y-1,0)))
                if grid[min(x+1,row-1)][y] == 1:
                    grid[min(x+1,row-1)][y] = 2
                    flag = True
                    queue.append((min(x+1,row-1),y))
                if grid[x][min(y+1,col-1)] == 1:
                    grid[x][min(y+1,col-1)] = 2
                    flag = True
                    queue.append((x,min(y+1,col-1)))
            if flag:
                day += 1
            else:
                if not check(row,col,grid):
                    return -1
                return day   
        
        return day'''