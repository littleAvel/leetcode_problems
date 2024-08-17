from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        smallest = arrays[0][0]
        largest = arrays[0][-1]
        res = 0

        for i in range(1, len(arrays)):
            arr = arrays[i]
            res = max(res, abs(largest - arr[0]), abs(arr[-1] - smallest))
            smallest = min(smallest, arr[0])
            largest = max(largest, arr[-1])

        return res