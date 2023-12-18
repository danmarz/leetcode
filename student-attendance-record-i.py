class Solution:
    def checkRecord(self, s: str) -> bool:
        # Check if the count of 'A's is less than 2
        if s.count("A") >= 2:
            return False

        # Search for the pattern 'LLL'
        if "LLL" in s:
            return False

        return True
