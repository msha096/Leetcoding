class TrieNode():
    def __init__(self):
        self.child = {}
        self.isend = False
class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        #self.isend = '*'
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        node = self.root
        for w in word:
            if w not in node.child:
                node.child[w] = TrieNode()
            node = node.child[w]
        node.isend = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.helper(self.root,word,0)
    
    def helper(self,node,word,ind):
        
        # DFS 
        if ind == len(word):
            return node.isend 
        if word[ind] == '.':
            for key in node.child:
                if self.helper(node.child[key],word,ind+1):
                    return True
            return False
        else:
            if word[ind] not in node.child:
                return False
            return self.helper(node.child[word[ind]],word,ind+1)
'''
class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.isend = '*'
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        node = self.root
        for w in word:
            if w not in node:
                node[w] = {}
            node = node[w]
        node[self.isend] = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.helper(self.root,word,0)
    
    def helper(self,node,word,ind):
        #print word, ind, node.child
        print(node)
        if ind == len(word):
            print (node)
            return self.isend in node 
        if word[ind] == '.':
            for key in node:
                if key == self.isend:
                    continue
                if self.helper(node[key],word,ind+1):
                    return True
            return False
        else:
            if word[ind] not in node:
                return False
            return self.helper(node[word[ind]],word,ind+1)
'''
        