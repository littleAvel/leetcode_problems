from typing import List

# Counting sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        max_n, min_n = max(nums) + 1, min(nums) - 1
        min_n = 0 if min_n >= 0 else min_n
        pos, neg = [0] * max_n, [0] * abs(min_n)

        for i in nums:
            if i >= 0:
                pos[i] += 1
            else:
                neg[abs(i)] += 1
        res = []
        for i in range(len(neg)-1, -1, -1):
            if neg[i]:
                res.extend([-i]*neg[i])
        for i in range(len(pos)):
            if pos[i]:
                res.extend([i]*pos[i])
        return res
    
# Selection sort
# Time limit exceeded.
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            min_ind = i
            for j in range(i+1, len(nums)):
                if nums[min_ind] > nums[j]:
                    min_ind = j
            nums[min_ind], nums[i] = nums[i], nums[min_ind]
        return nums

# Bubble Sort
# Time Limit Exceeded
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i] > nums[j]:
                    nums[j], nums[i] = nums[i], nums[j]
        return nums

# Insertion Sort
# Time Limit Exceeded
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            key = nums[i]
            j = i - 1
            
            while j >= 0 and key < nums[j]:
                nums[j+1] = nums[j]
                j -= 1
            nums[j+1] = key
        return nums
    
# Merge Sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums

        mid = len(nums) // 2

        L = nums[:mid]
        R = nums[mid:]

        self.sortArray(L)
        self.sortArray(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                nums[k] = L[i]
                i += 1
            else:
                nums[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            nums[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            nums[k] = R[j]
            j += 1
            k += 1
        
        return nums