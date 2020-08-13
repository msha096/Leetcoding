class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        
        '''
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        queue = [1,1]
        for i in range(1,rowIndex):
            size = len(queue)
            #queue.append(1)
            prev = 0
            for j in range(size):
                cur = queue.pop(0)
                queue.append(prev+cur)
                prev = cur
            queue.append(1)
        return queue'''
    
        # recursive
        if rowIndex == 0: return [1]
        prev = self.getRow(rowIndex-1)
        return [1] + [prev[i]+prev[i+1] for i in range(len(prev)-1)] + [1]