class Solution:
    def myAtoi(self, s: str) -> int:
        nums = "0123456789"
        signs = "+-"
        res, sign = 0, 1
        stripped = s.lstrip()
        if stripped == "":
            return res * sign

        if stripped[0] in signs:
            sign = -1 if stripped[0] == "-" else 1
            stripped = stripped[1:]

        for i in range(len(stripped)):
            if stripped[i] not in nums:
                break

            if stripped[i] != "0":
                stripped = stripped[i:]
                break

        for i in stripped:
            if i not in nums:
                break

            if res == 0:
                res = int(i)
            else:
                res *= 10
                res += int(i)

        if res >= 2**31:
            res = 2**31 if sign == -1 else 2**31 - 1

        return res * sign
