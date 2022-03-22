class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        sortedorder = []
        if numCourses <= 0:
            return False
        
        inDegree = {i : 0 for i in range(numCourses)}
        graph = {i : [] for i in range(numCourses)}
        
        for child, parent in prerequisites:
            graph[parent].append(child)
            inDegree[child] += 1
            
        sources = deque()
        
        for key in inDegree:
            if inDegree[key] == 0:
                sources.append(key)
        while sources:
            vertex = sources.popleft()
            sortedorder.append(vertex)
            for child in graph[vertex]:
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    sources.append(child)
                    
        if len(sortedorder) != numCourses:
            return []
        return sortedorder
        
    def findOrder1(self, numCourses, prerequisites):
        #dic[i] is the indegree of node i
        dic = [0 for i in range(numCourses)]
        neigh = collections.defaultdict(set)
        for i, j in prerequisites:
            dic[i] += 1
            neigh[j].add(i)
        stack = [i for i in range(numCourses) if dic[i] == 0]
        res = []
        while stack:
            node = stack.pop()
            res.append(node)
            for i in neigh[node]:
                dic[i] -= 1
                if dic[i] == 0:
                    stack.append(i)
                    
        for i in range(numCourses):
            if dic[i] > 0:
                return []
        return res