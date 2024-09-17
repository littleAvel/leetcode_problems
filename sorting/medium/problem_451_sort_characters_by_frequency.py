# Bucket Sort
class Solution:
    def frequencySort(self, s: str) -> str:
        counter = {}
        max_freq = 0
        for ch in s:
            counter[ch] = counter.get(ch, 0) + 1
            max_freq = max(max_freq, counter[ch])
        
        buckets = [[] for _ in range(max_freq + 1)]
        for ch, count in counter.items():
            buckets[count].append(ch)
        
        result = ""
        for i in range(max_freq, 0, -1):
            for ch in sorted(buckets[i]):
                result += (ch * i)

        return result