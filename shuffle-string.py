class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = ["" for i in range(len(s))]

        # Alternative, faster. However if the elements were mutable (e.g., lists instead of strings), modifying one would affect all,
        # because they share the same reference. However, since strings are immutable, this doesn’t cause issues in this specific case.
        # ans = [ "" ] * len(s)

        for pos, index in enumerate(indices):
            ans[index] = s[pos]

        return "".join(ans)
