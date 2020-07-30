class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # use the indegree to store the number of prerequisites 
        graph = {u:[] for u in range(numCourses)}
        v = []
        indegree = [0]*(numCourses)
        
        for k in prerequisites:
            graph[k[1]].append(k[0])
            v.append(k[0])
            indegree[k[0]] += 1
        
        queue = []
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        res = [] # the order of course taking
        while queue:
            top = queue.pop(0) # BFS
            res.append(top)
            for node in graph[top]:
                indegree[node] -= 1
                if indegree[node] == 0: # after finishing all the pre-courses, indegree is 0, add to the queue and wait to be taken
                    queue.append(node)
        if len(res) != numCourses:
            return []
        return res
                
        '''
        This solution works, but the time complexity is not good!
        graph = {u:[] for u in range(numCourses)}
        request = {u:[] for u in range(numCourses)}
        v = []
        
        for k in prerequisites:
            graph[k[1]].append(k[0])
            v.append(k[0])
            request[k[0]].append(k[1])
        
        
        
        #print(graph)
        #print(v)
        #print(request)
        Q = []
        for i in range(numCourses):
            if i not in v:
                Q.append(i)
        res = []
        
        while Q:
            top = Q.pop(0)
            res.append(top)
            for node in graph[top]:
                if node not in Q and node not in res:
                    flag = True
                    for every_pre in request[node]:
                        if every_pre not in res:
                            flag = False
                    if flag:
                        Q.append(node)
                    #heapq.heappush(Q,node)
        if len(res)!=numCourses:
            return []
        return res'''