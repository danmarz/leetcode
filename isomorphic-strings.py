class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_map = {}  # Dictionary to store character mappings from s to t

        for i in range(len(s)):
            if s[i] in char_map:
                # If the character in s is already mapped to a different character in t, it's not isomorphic
                if char_map[s[i]] != t[i]:
                    return False
            else:
                # If the character in s is not in the dictionary, but the corresponding character in t is used by another character in s, it's not isomorphic
                if t[i] in char_map.values():
                    return False
                char_map[s[i]] = t[i]  # Map the character in s to the character in t

        return True  # If we reach this point, s and t are isomorphic
