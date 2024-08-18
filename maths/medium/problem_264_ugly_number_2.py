# Solution 1
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        list1 = [0] * n
        list1[0] = 1
        a = b = c = 0

        for i in range(1, n):
            list1[i] = min(list1[a] * 2, list1[b] * 3, list1[c] * 5)
            if list1[a] * 2 == list1[i]:
                a += 1
            if list1[b] * 3 == list1[i]:
                b += 1
            if list1[c] * 5 == list1[i]:
                c += 1

        return list1[n - 1]


# Solution 2 - Using Set
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_nums = set()
        ugly = 1
        ugly_nums.add(ugly)

        for i in range(n):
            ugly = min(ugly_nums)
            ugly_nums.remove(ugly)

            ugly_nums.add(ugly * 2)
            ugly_nums.add(ugly * 3)
            ugly_nums.add(ugly * 5)

        return ugly


# Solution 3 - Min-Heap/Priority Queue
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_nums = set()
        ugly = 1
        ugly_nums.add(ugly)

        for i in range(n):
            ugly = min(ugly_nums)
            ugly_nums.remove(ugly)

            ugly_nums.add(ugly * 2)
            ugly_nums.add(ugly * 3)
            ugly_nums.add(ugly * 5)

        return ugly


# Solution 4 - Dynamic Programming (DP)
import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_nums = [0] * n
        ugly_nums[0] = 1

        index2, index3, index5 = 0, 0, 0
        next2, next3, next5 = 2, 3, 5

        for i in range(1, n):
            next_ugly = min([next2, next3, next5])
            ugly_nums[i] = next_ugly

            if next_ugly == next2:
                index2 += 1
                next2 = ugly_nums[index2] * 2
            if next_ugly == next3:
                index3 += 1
                next3 = ugly_nums[index3] * 3
            if next_ugly == next5:
                index5 += 1
                next5 = ugly_nums[index5] * 5

        return ugly_nums[n - 1]