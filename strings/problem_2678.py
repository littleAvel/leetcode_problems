from typing import List


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for i in range(len(details)):
            if details[i][11:13] > "60":
                count += 1
        return count