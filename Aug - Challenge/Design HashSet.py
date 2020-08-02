class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        #self.l = [False for i in range(1000000)]
        self.l = [[] for i in range(1000)]
        
    def hashkey(self,key):
        # hash mapping
        return key % 1000
    
    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        #self.l[key] = True
        if not self.contains(key):
            hk = self.hashkey(key)
            self.l[hk].append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        hk = self.hashkey(key)
        if key in self.l[hk]:
            self.l[hk].remove(key)
        
    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        hk = self.hashkey(key)
        return key in self.l[hk]
        #return self.l[key]