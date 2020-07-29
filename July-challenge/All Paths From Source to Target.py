class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        # dfs algo, once reach the target, add it to the returned result
        # otherwise, self recursive with neighbors
        # no need to construct graph in this question
        def dfs(formed):
            if formed[-1]==n-1:
                res.append(formed)
                return
            for k in graph[formed[-1]]:
                dfs(formed+[k])
        res = []
        n = len(graph)
        dfs([0])
        return res
    
    '''n = len(graph)
        g = {u:[] for u in range(n)}
        
        for i in range(n):
            for k in graph[i]:
                if i==0:
                    g[i].append([0,k])
                else:
                    g[i].append([k])
                #g[k].append(i)
        #print(g)
        queue = g[0]
        #print(queue)
        ret = []
        #res = [0]
        while queue:
            #print(queue,'res',res,'ret',ret)
            top = queue.pop(0) # BFS # just pop() -> DFS
            #print('top',top)
            #res.append(top)
            if n-1 in top:
                if top in ret:
                    #res = [0]
                    continue
                ret.append(top)
                #res = [0]
            for v in g[top[-1]]:
                #print('v',v)
                res = top[::]
                res+=(v)
                queue.append(res)
        return ret'''