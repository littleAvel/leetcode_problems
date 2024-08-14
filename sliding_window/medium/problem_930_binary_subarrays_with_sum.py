from typing import List

class Solution:
    def count(self, nums: List[int], goal: int) -> int:
        if goal < 0: return 0

        l, r = 0, 0
        sub_sum, count = 0, 0

        while r < len(nums):
            sub_sum += nums[r]

            while sub_sum > goal:
                sub_sum -= nums[l]
                l += 1
            
            count = count + (r - l + 1)
            r += 1
        return count

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.count(nums, goal) - self.count(nums, goal-1)