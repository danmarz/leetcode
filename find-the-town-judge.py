class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Initialize arrays to count trust relationships
        trust_count = [0] * (n + 1)  # Index 0 is not used
        trusted_by_count = [0] * (n + 1)  # Index 0 is not used

        # Iterate through trust relationships and update counts
        for a, b in trust:
            trust_count[a] += 1
            trusted_by_count[b] += 1

        # Find the town judge
        for i in range(1, n + 1):
            if trust_count[i] == 0 and trusted_by_count[i] == n - 1:
                return i  # Found the town judge

        return -1  # Town judge not found
