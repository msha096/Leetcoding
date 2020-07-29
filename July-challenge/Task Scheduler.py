class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # first idea was to use priority queue, considering the cooling time and frequence of the task
        # however that solution is TLE.

        # the following solution: with O(n) time complexity
        # 1. count the frequence, (could use counter())
        # 2. find the task with the maximum frequence k
        # 3. create k groups with each lenghth of n
        # 4. fill the avaliable slots and judge (providing two methods)
        freq = [0 for i in range(26)]
        for k in tasks:
            freq[ord(k) - ord('A')]+=1
        #print(freq)
        freq.sort()
        max_val = freq[-1]
        ''' 
        # method 1
        max_count = 0 
        for i in freq:
            if i == max_val:
                max_count += 1
        ans = (max_val -1) * (n+1) + max_count #divide into slot, group. 
        return max(ans,len(tasks)) # maybe too many low freq...'''
        
        # method 2 
        avaliable = (max_val -1)*n
        for i in freq[:-1]:
            avaliable -= min(i, max_val-1)
        if avaliable > 0:
            return avaliable +len(tasks)
        
        return len(tasks)


        '''#TLE
        d = defaultdict(int)
        for i in tasks:
            d[i]+=1
        
        q = []
        for key in d:
            heapq.heappush(q,[0,-d[key],key])
        #print q

        time = 0
        
        def helper(q):
            for each in q:
                if each[0]>0:
                    each[0]-=1
            q.sort()
        while q:
            #print(q)
            top = heapq.heappop(q)
            time += 1
            #print(time,top)
            
            if top[0]!=0:
                heapq.heappush(q,top)
                helper(q)
            else:   
                helper(q)
                if top[1]==-1:   # this task finish, no need to put back
                    continue
                top[1] += 1
                top[0] = n
                heapq.heappush(q,top)
            
        return time'''
    