class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1.0
        if n == 0: return res

        x_sign, n_sign = (-1 if (x < 0 and n % 2) else 1), (-1 if n < 0 else 1)
        x, n = abs(x), abs(n)

        while n > 1:
            if n % 2:
                res *= x
                n -= 1
            else:
                x *= x
                n //= 2
        res *= x
        res *= x_sign

        return res if n_sign == 1 else 1/res
