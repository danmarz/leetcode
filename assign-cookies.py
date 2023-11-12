class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # Sort the greed factors and cookie sizes.
        g.sort()
        s.sort()

        content_children = 0  # Counter for content children.
        cookie_index = 0  # Index to iterate through cookie sizes.

        # Iterate through greed factors and assign cookies to children.
        for greed in g:
            while cookie_index < len(s) and s[cookie_index] < greed:
                cookie_index += 1

            # If there are available cookies, assign one to the current child.
            if cookie_index < len(s):
                content_children += 1
                cookie_index += 1

        return content_children
