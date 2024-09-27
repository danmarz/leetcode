class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        result = [0] * n  # Initialize result array with zeros

        if k == 0:
            return result  # If k is zero, return all zeros

        for i in range(n):
            total = 0
            if k > 0:
                for j in range(1, k + 1):
                    total += code[(i + j) % n]  # Sum the next k elements circularly
            else:
                for j in range(1, -k + 1):
                    total += code[(i - j) % n]  # Sum the previous k elements circularly
            result[i] = total

        return result
