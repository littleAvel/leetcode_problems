class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        self.visited = [False] * n
        self.inStack = [False] * n

        def dfs(node):
            if self.inStack[node]:
                return True
            if self.visited[node]:
                return False

            self.visited[node] = True
            self.inStack[node] = True

            neighbours = graph[node]
            for next_node in neighbours:
                if dfs(next_node):
                    return True
            
            self.inStack[node] = False
            return False
        
        for i in range(n):
            dfs(i)

        safeNodes = []
        for i in range(n):
            if not self.inStack[i]:
                safeNodes.append(i)
        return safeNodes
