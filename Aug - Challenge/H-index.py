class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True)
            
        for h in range(len(citations)):
            if citations[h]>=h+1 and citations[h]>0:
                continue
            else:
                if h ==0:
                    return 0
                else:
                    return h
        return len(citations)