from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res, odd = 0, 0
        l, m = 0, 0
        n = len(nums)

        for i in range(n):
            nums[i] = nums[i]%2

        for r in range(n):
            if nums[r]:
                odd += 1

            while odd > k:
                if nums[l]:
                    odd -= 1
                l += 1
                m = l
            if odd == k:
                while not nums[m]:
                    m += 1
                res += (m - l) + 1
        return res