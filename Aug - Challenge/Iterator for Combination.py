class CombinationIterator(object):

    def __init__(self, characters, combinationLength):
        """
        :type characters: str
        :type combinationLength: int
        """
        self.res = []
        
        '''def combination(characters, begin, k, combinationLength, out, res):
            if k == combinationLength:
                self.res.append(''.join(out))
                return
            if begin == len(characters):
                return
            out.append(characters[begin])
            combination(characters, begin+1, k+1, combinationLength, out, res)
            out.pop()
            combination(characters, begin+1, k, combinationLength, out, res)'''
            
        def combine(s, ind, com):
            if len(com) == combinationLength:
                self.res.append(com)
                return
            if ind >=len(s):
                return
            for i in range(ind,len(s)):
                combine(s,i+1,com+s[i])
        #out = []
        #combination(characters,0,0,combinationLength,out,self.res)
        combine(characters,0,'')
        self.ind = -1
       

    def next(self):
        """
        :rtype: str
        """
        self.ind += 1
        if self.hasNext() or self.ind == len(self.res)-1:
            return self.res[self.ind]

    def hasNext(self):
        """
        :rtype: bool
        """

        return self.ind<len(self.res)-1


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()