from typing import List

# Solution #1 
# Bucket Sort

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = [False] * (60 * 24)
        for time in timePoints:
            h, m = time.split(':')
            min_time = int(h) * 60 + int(m)
            if minutes[min_time]:
                return 0
            minutes[min_time] = True

        prevIndex = float("inf")
        firstIndex, lastIndex = float("inf"), float("inf")
        ans = float("inf")

        for i in range(24 * 60):
            if minutes[i]:
                if prevIndex != float("inf"):
                    ans = min(ans, i - prevIndex)
                prevIndex = i

                if firstIndex == float("inf"):
                    firstIndex = i
                lastIndex = i

        return min(ans, 24 * 60 - lastIndex + firstIndex)

# Solution #2
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        time_in_min = []
        max_diff = 24 * 60
        min_diff = 24 * 60

        for time in timePoints:
            h, m = time.split(':')
            minutes = int(h) * 60 + int(m)
            time_in_min.append(minutes)
        time_in_min.sort()
        print(time_in_min)

        for i in range(1, len(time_in_min)):
            min_diff = min(min_diff, time_in_min[i] - time_in_min[i - 1])
        
        min_diff = min(min_diff, time_in_min[0] + (max_diff - time_in_min[-1]))

        return min_diff