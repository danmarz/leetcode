class Solution:
    def sortString(self, s: str) -> str:
        s = list(s)
        result = []

        while s:
            # Step 1, 2: Pick smallest character and next smallest greater characters
            smallest_chars = []
            smallest = None
            for ch in sorted(set(s)):
                if smallest is None or ch > smallest:
                    smallest = ch
                    smallest_chars.append(ch)

            for ch in smallest_chars:
                result.append(ch)
                s.remove(ch)

            # Step 3, 4: Pick largest character and next largest smaller characters
            largest_chars = []
            largest = None
            for ch in sorted(set(s), reverse=True):
                if largest is None or ch < largest:
                    largest = ch
                    largest_chars.append(ch)

            for ch in largest_chars:
                result.append(ch)
                s.remove(ch)

        return "".join(result)
