from typing import List

# Counting sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        max_n, min_n = max(nums) + 1, min(nums) - 1
        min_n = 0 if min_n >= 0 else min_n
        pos, neg = [0] * max_n, [0] * abs(min_n)

        for i in nums:
            if i >= 0:
                pos[i] += 1
            else:
                neg[abs(i)] += 1
        res = []
        for i in range(len(neg)-1, -1, -1):
            if neg[i]:
                res.extend([-i]*neg[i])
        for i in range(len(pos)):
            if pos[i]:
                res.extend([i]*pos[i])
        return res
