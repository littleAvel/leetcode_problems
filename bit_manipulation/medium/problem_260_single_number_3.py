from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        b1, b2 = 0, 0
        for num in nums:
            xor ^= num
        
        right_most = (xor & (xor - 1)) ^ xor

        for num in nums:
            if num & right_most:
                b1 ^= num
            else:
                b2 ^= num
        return [b1, b2]