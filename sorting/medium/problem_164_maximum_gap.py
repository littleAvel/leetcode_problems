# Bucket Sort
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2: return 0

        low, high = min(nums), max(nums)
        b_dict = defaultdict(list)
        for num in nums:
            if num == high:
                ind = n - 1
            else:
                ind = (abs(low - num) * (n - 1)) // (high - low)
            b_dict[ind].append(num)

        buckets = []
        for i in range(n):
            if b_dict[i]:
                buckets.append((min(b_dict[i]), max(b_dict[i])))

        max_gap = 0
        for i in range(1, len(buckets)):
            max_gap = max(max_gap, abs(buckets[i-1][-1] - buckets[i][0]))

        return max_gap
