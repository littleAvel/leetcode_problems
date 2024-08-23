from typing import List


class Solution:
    def computeGCD(self, x: str, y: str) -> str:
        while(y):
            x, y = y, x % y
        return abs(x)

    def computeLCM(self, arr: List[int]) -> int:
        lcm = 1
        for i in arr:
            lcm = lcm * i // self.computeGCD(lcm, i)
        return lcm

    def fractionAddition(self, expression: str) -> str:
        expressions = []
        denominators = []

        # Parse the expression into numerators and denominators
        num_start = 0
        for i in range(1, len(expression)):
            if expression[i] in "+-":
                exp = expression[num_start:i]
                expressions.append(exp)
                denominators.append(int(exp.split('/')[-1]))
                num_start = i
        expressions.append(expression[num_start:])  # Append the last fraction
        denominators.append(int(expression[num_start:].split('/')[-1]))

        # Compute LCM of all denominators
        lcm = self.computeLCM(denominators)
        res = 0

        # Sum up the fractions after converting them to a common denominator (lcm)
        for exp in expressions:
            num, denom = map(int, exp.split('/'))
            res += (lcm // denom) * num

        # Simplify the resulting fraction
        gcd_res = self.computeGCD(res, lcm)
        ans = f"{res // gcd_res}/{lcm // gcd_res}"

        return ans
