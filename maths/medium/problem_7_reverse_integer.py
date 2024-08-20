# Solution #1
class Solution:
    def reverse(self, x: int) -> int:
        sign = [1, -1][x < 0]
        rev, x = 0, abs(x)

        while x:
            x, mod = divmod(x, 10)
            rev = rev * 10 + mod
            if rev > 2**31 - 1:
                return 0
        return sign * rev

# Solution #2
class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = str(x)[1:] if x < 0 else str(x)

        num = x[::-1]
        res = int(num) * sign
        return res if (-2) ** 31 <= res <= (2**31) - 1 else 0