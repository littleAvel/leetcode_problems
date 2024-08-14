class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        edge_count = [0] * n
        res, label = 0, 1
        for n1, n2 in roads:
            edge_count[n1] += 1
            edge_count[n2] += 1

        for count in sorted(edge_count):
            res += count * label
            label += 1
        return res
