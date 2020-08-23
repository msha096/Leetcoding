class StreamChecker(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.Trie = {}
        self.prefix = '' # to store each query's letter
        self.max = 0
        for word in words:
            if len(word)>self.max:
                self.max = len(word)
            word = word[::-1] # reverse and stored into Trie
            d = self.Trie
            for l in word:
                if l not in d:
                    d[l] = {}
                d = d[l]
            d['#'] = True # end of the word
        #print self.Trie

    def query(self, letter):
        """
        :type letter: str
        :rtype: bool
        """
        self.prefix += letter
        if len(self.prefix) > self.max:
            self.prefix = self.prefix[-self.max:]
        d = self.Trie
        
        for i in range(len(self.prefix)-1,-1,-1):
            if self.prefix[i] in d:
                if '#' in d[self.prefix[i]]:
                    return True
                d = d[self.prefix[i]]
            else:
                return False
        return False