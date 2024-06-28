# solution 1
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return edges[0][0] if edges[0][0] in edges[1] else edges[0][1]
    
# solution 2
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        edges_count = [0] * (len(edges)+2)
        for n1, n2 in edges:
            edges_count[n1] += 1
            edges_count[n2] += 1

        return edges_count.index(max(edges_count))