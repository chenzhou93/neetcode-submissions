class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return False

        stack = []
        for char in s:
            if char in ('(', '{', '['):
                stack.append(char)
            elif char == ')':
                if len(stack) > 0:
                    r = stack.pop()
                    if r != '(':
                        return False
                else:
                    return False
            elif char == ']':
                if len(stack) > 0:
                    r = stack.pop()
                    if r != '[':
                        return False
                else:
                    return False
            elif char == '}':
                if len(stack) > 0:
                    r = stack.pop()
                    if r != '{':
                        return False
                else:
                    return False
        return len(stack) == 0
        