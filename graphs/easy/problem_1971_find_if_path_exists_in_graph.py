# TODO: review this code later
# Solution 1
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True

        graph = defaultdict(list)
        print(graph)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        seen = set()
        seen.add(source)

        def dfs(i):
            if i == destination:
                return True
            
            for node in graph[i]:
                if node not in seen:
                    seen.add(node)
                    if dfs(node):
                        return True
            return False

        return dfs(source)

# Solution 2
class Solution(object):
    def validPath(self, n, edges, source, destination):
        def add_dict(dictionary_list, dictionary_item, dictionary_VisitedContainer):
            if dictionary_item in dictionary_list:
                dictionary_list[dictionary_item].append(dictionary_VisitedContainer)
            else:
                dictionary_list[dictionary_item] = [dictionary_VisitedContainer]
        dictionary_list = dict()
        for edge in edges:
            matrix_col=edge[1]
            matrix_row=edge[0]
            add_dict(dictionary_list, matrix_row, matrix_col)
            add_dict(dictionary_list, matrix_col, matrix_row)
			 
        if n==1: return True
        if source not in dictionary_list or destination not in dictionary_list: return False

        listOfStartPoints= [source]
        visited = set() 
        while listOfStartPoints:
            node_afterRemoval = listOfStartPoints.pop(0) 
            if destination in dictionary_list[node_afterRemoval]:
                return True
            else:
                visited.add(node_afterRemoval)
                for ChildNode_afterRemoval in dictionary_list[node_afterRemoval]: 
                    if ChildNode_afterRemoval not in visited:
                        listOfStartPoints.append(ChildNode_afterRemoval)
        return False   