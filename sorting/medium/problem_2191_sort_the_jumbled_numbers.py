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


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapped = {}
        pairs, answer = [], []
        mapped = [mapping[i] for i in range(len(mapping))]

        for i in range(len(nums)):
            s = ''.join(str(mapped[int(j)]) for j in str(nums[i]))
            mapped_num = int(s)
            pairs.append([i, mapped_num])

        pairs.sort(key=lambda x: list(x)[1])

        return [nums[pair[0]] for pair in pairs]