from typing import List

# Solution #1
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_ind = 0
        for i in range(len(nums)):
            if max_ind < i:
                return False
            max_ind = max(max_ind, i + nums[i])
        return True
    
# Solution #2
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0
