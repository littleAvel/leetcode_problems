# Bucket Sort
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        n = len(words)
        words_count = {}
        buckets = [[] for _ in range(n + 1)]

        for word in words:
            words_count[word] = words_count.get(word, 0) + 1

        for word, count in words_count.items():
            buckets[count].append(word)

        result = []
        for i in range(n, 0, -1):
            for item in sorted(buckets[i]):
                result.append(item)
                if len(result) == k:
                    return result
    
        return result