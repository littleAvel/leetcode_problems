
# Solution #1
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1, num2 = [num2, num1] if len(num1) < len(num2) else [num1, num2]
        lst = []

        for i in range(len(num1) - 1, -1, -1):
            res = ""
            carry = 0
            for j in range(len(num2) - 1, -1, -1):
                val = int(num2[j]) * int(num1[i]) + carry
                carry, val = divmod(val, 10)
                res += str(val)
            if carry: res += str(carry)

            zeros = len(num1) - 1 - i
            num = int(res[::-1] + '0' * zeros)
            lst.append(num)

        return str(sum(lst))

# Solution #2
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if '0' in [num1, num2]:
            return '0'

        res = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]
    
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])
                res[i1 + i2] += digit
                res[i1 + i2 + 1] += (res[i1 + i2] // 10)
                res[i1 + i2] = res[i1 + i2] % 10

        res, beg = res[::-1], 0
        while beg < len(res) and res[beg] == 0:
            beg += 1

        res = map(str, res[beg:])
        return "".join(res)