# review this problem later
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        num_size = len(nums)
        if num_size <= 4:
            return 0
        
        nums.sort()
        min_diff = float("inf")

        for left in range(4):
            right = num_size - 4 + left
            min_diff = min(min_diff, nums[right] - nums[left])

        return min_diff
