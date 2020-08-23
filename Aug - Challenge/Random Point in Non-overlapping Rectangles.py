class Solution(object):

    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        # choose ith rect by considering the space
        # chosoe the point inside the ith rect
        
        self.rect = rects
        self.weight = []
        w = 0
        for pair in rects:
            k = (pair[2]-pair[0]+1)*(pair[3]-pair[1]+1)
            w += k
            self.weight.append((w-k+1,w))
        
        
        

    def pick(self):
        """
        :rtype: List[int]
        """
        n = random.randint(1,self.weight[-1][1])
        for i in range(len(self.weight)):
            if self.weight[i][0]<=n<=self.weight[i][1]:
                return [random.randint(self.rect[i][0],self.rect[i][2]),random.randint(self.rect[i][1],self.rect[i][3])]