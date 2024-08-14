# TODO: review this problem later
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        connections = defaultdict(list)
        for a, b in redEdges:
            connections[a].append((b, 'red'))
        for a, b in blueEdges:
            connections[a].append((b, 'blue'))

        distances = [math.inf] * n
        queue = deque([(0, 'red', 0), (0, 'blue', 0)])
        visited = set()
        while queue:
            node, color, level = queue.popleft()

            if (node, color) in visited:
                continue
            visited.add((node, color))

            distances[node] = min(distances[node], level)

            for next_node, next_color in connections[node]:
                if next_color != color:
                    queue.append((next_node, next_color, level + 1))

        return [-1 if x == math.inf else x for x in distances]
        