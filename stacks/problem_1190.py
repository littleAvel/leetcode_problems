class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for i in s:
            if i == ')':
                portion = []
                while stack [-1] != '(':
                    portion.append(stack.pop())
                stack.pop()
                stack.extend(portion)
            else:
                stack.append(i)
        return "".join(stack)