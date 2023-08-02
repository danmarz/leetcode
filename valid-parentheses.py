class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        char_map = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in char_map.values():
                stack.append(char)
            elif char in char_map.keys():
                if stack and stack[-1] == char_map[char]:
                    stack.pop()
                else:
                    return False
            else:
                return False

        return not stack
