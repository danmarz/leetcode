class Solution:
    def countSegments(self, s: str) -> int:
        # create a list based on a space split
        slist = list(s.split(" "))

        # return the len of list minus empty item
        return len(slist) - slist.count("")

        # Alternative, bruteforce:
        """
        s = s.strip()
        
        count = 0
        
        if len(s) == 0:
            return 0
        
        for pos, char in enumerate(s):
            if char == ' ' and s[pos + 1] != ' ':
                count += 1        
        
        return count + 1
        """
