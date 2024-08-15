from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        counter = { 5: 0, 10: 0 }
        
        for bill in bills:
            if bill == 5:
                counter[bill] += 1
            elif bill == 10:
                if counter[5] == 0:
                    return False
                counter[5] -= 1
                counter[bill] += 1
            else:
                if counter[5] > 0 and counter[10] > 0:
                    counter[5] -= 1
                    counter[10] -= 1
                elif counter[5] >= 3:
                    counter[5] -= 3
                else:
                    return False
        return True