class Solution:
    def isValid(self, s: str) -> bool:
        s_len = len(s)
        if s_len == 0 or s_len % 2 != 0:
            return False

        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if top_element != mapping[char]:
                    return False
            else:
                stack.append(char)
            
        if stack == []:
            return True
        else:
            return False