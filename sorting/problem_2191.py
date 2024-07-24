from typing import List


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        store_pairs = []

        for i in range(len(nums)):
            mapped_value = 0
            temp = nums[i]

            place = 1
            if temp == 0:
                store_pairs.append((mapping[0], i))
                continue
            while temp != 0:
                mapped_value = place * mapping[temp % 10] + mapped_value
                place *= 10
                temp //= 10
            store_pairs.append((mapped_value, i))

        store_pairs.sort()
        answer = [nums[pair[1]] for pair in store_pairs]

        return answer