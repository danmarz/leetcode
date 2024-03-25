class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        # Initialize pointers for both strings
        i, j = 0, 0

        # Loop through both strings
        while j < len(typed):
            # If characters match, move both pointers forward
            if i < len(name) and name[i] == typed[j]:
                i += 1
                j += 1
            # If characters don't match and the current character in typed
            # is the same as the previous one, it's a long-pressed key,
            # so move to the next character in typed
            elif j > 0 and typed[j] == typed[j - 1]:
                j += 1
            # If characters don't match and it's not a long-pressed key,
            # return False
            else:
                return False

        # If we've reached the end of both strings, return True
        return i == len(name)
