class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last_seen = {i: -1 for i in "abc"}
        count, n = 0, len(s)

        for i in range(n):
            last_seen[s[i]] = i
            if last_seen['a'] != -1 and last_seen['b'] != -1 and last_seen['c'] != -1:
                count = count + (1 + min(last_seen.values()))
        return count