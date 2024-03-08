class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def apply_backspace(string: str) -> str:
            stack = []
            for char in string:
                if char != "#":
                    stack.append(char)
                elif stack:
                    stack.pop()
            return "".join(stack)

        return apply_backspace(s) == apply_backspace(t)

        # Bruteforce alternative
        """    
        newS = ""
        newT = ""
        
        for char in s:
            if char == '#':
                newS = newS[:-1]
                continue
            newS += char
        
        for char in t:
            if char == '#':
                newT = newT[:-1]
                continue
            newT += char
        
        return newS == newT
        """
