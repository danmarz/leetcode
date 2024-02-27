class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        double_s = s + s
        return goal in double_s

        # Alternative solution
        """
        for i in range(len(goal)):
            if s == goal:
                return True
            else:
                s = s[1:] + s[0]
        return False
        """
