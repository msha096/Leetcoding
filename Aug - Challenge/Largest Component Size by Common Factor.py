class UnionFind(object):
    def __init__(self,n):
        self.uf = [i for i in range(n+1)]
        
    def find(self,x):
        if x!=self.uf[x]:
            self.uf[x] = self.find(self.uf[x])
        return self.uf[x]
    
    def union(self,x,y):
        self.uf[self.find(x)] = self.uf[self.find(y)]
        
class Solution(object):
    def largestComponentSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = max(A)
        uf = UnionFind(n)
        for num in A:
            for i in range(2,int(num**0.5)+1):
                if num%i == 0:
                    uf.union(num,i)
                    uf.union(num,num/i)
                    #print num,i,uf.uf
        counter = defaultdict(int)
        ans = 0
        #print uf.uf
        for num in A:
            p = uf.find(num)
            counter[p] += 1
            ans = max(ans,counter[p])
        #print counter
        return ans
        '''# TLE should use union-find
        def factor(k,num):
            if num <2:
                return k
            for i in range(2,int(num**0.5)+1):
                if num % i == 0:
                    if k[i] == False:
                        k[i] = [num]
                    else:
                        k[i].append(num)
                    if k[num/i] == False:
                        k[num/i] = [num]
                    else:
                        k[num/i].append(num)
                        
            if k[num]==False:
                k[num] = [num]
            else:
                k[num].append(num)
            return k
        
        graph = {u:[] for u in A}
        
        k = [False]*(max(A)+1)
        for a in A:
            k = factor(k,a)
        #print k
        for p in k:
            if p == False:
                continue
            for i in range(len(p)):
                graph[p[i]] += p
                graph[p[i]].remove(p[i])
        #print graph        
        
        def dfs(cur, totalNum, seen):
            q = graph[cur]
            seen.add(cur)
            while q:
                nxt = q.pop()
                if nxt not in seen:
                    seen.add(nxt)
                    if len(seen) == totalNum:
                        return totalNum
                    q += graph[nxt]
            return len(seen)
     
        
        d = 0
        for num in A:
            d = max(d,dfs(num,len(A),set()))
            if d == len(A):
                return d
        return d'''