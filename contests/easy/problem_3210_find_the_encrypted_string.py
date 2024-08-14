class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        res = ""
        n = len(s)
        for i in range(len(s)):
            res += s[(i+k)%n]
        return res