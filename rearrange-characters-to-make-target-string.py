class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        # Count character frequencies in both strings
        s_count = Counter(s)
        target_count = Counter(target)

        # Initialize result to a large number
        result = float("inf")

        # Loop through each character in target and calculate how many times it can appear from s
        for char, count in target_count.items():
            if char not in s_count:
                return 0  # If any character is missing, no copies can be formed
            result = min(result, s_count[char] // count)

        return result
