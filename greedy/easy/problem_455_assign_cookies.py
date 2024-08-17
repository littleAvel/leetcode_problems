from typing import List

# solution #1
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        content_children = 0
        cookie_index = 0

        while cookie_index < len(s) and content_children < len(g):
            if s[cookie_index] >= g[content_children]:
                content_children += 1
            cookie_index += 1
        
        return content_children

# solution #2
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        max_num = 0
        l, r = 0, len(s)

        for i in range(len(g)):
            while l < r and s[l] < g[i]:
                print("while")
                l += 1
            if l < r and s[l] >= g[i]:
                max_num += 1
                l += 1
            if l >= r:
                break
        return max_num