from collections import defaultdict
# TODO: review this problem later

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [defaultdict(int)]
        n = len(formula)
        
        i = 0
        while i < n:
            if formula[i] == '(':
                stack.append(defaultdict(int))
            elif formula[i] == ')':
                current_hash = stack.pop()
                prev_hash = stack[-1]
                count = ""
                while i + 1 < n and ('0' <= formula[i + 1] <= '9'):
                    i += 1
                    count += formula[i]
                count = 1 if not count else int(count)

                for key in current_hash.keys():
                    prev_hash[key] += current_hash[key] * count
            else:
                element = formula[i]
                count = ""
                if i + 1 < n and ('a' <= formula[i + 1] <= 'z'):
                    i += 1
                    element += formula[i]

                while i + 1 < n and ('0' <= formula[i + 1] <= '9'):
                    i += 1
                    count += formula[i]
                count = 1 if not count else int(count)

                current_hash = stack[-1]
                current_hash[element] += count

            i += 1

        result = ""
        res_hash = stack[-1]

        for key in sorted(res_hash.keys()):
            count = "" if res_hash[key] == 1 else str(res_hash[key])
            result += (key + count)

        return result