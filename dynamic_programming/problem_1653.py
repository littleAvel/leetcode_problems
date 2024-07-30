# TODO: review this solution
class Solution:
    def minimumDeletions(self, s: str) -> int:
        a_count = sum(1 for ch in s if ch == 'a')
        b_count = 0
        min_deletions = len(s)

        for ch in s:
            if ch == 'a':
                a_count -= 1
            min_deletions = min(min_deletions, a_count + b_count)
            if ch == 'b':
                b_count += 1
        return min_deletions