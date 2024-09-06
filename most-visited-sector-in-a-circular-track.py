class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        start = rounds[0]
        end = rounds[-1]

        if start <= end:
            # If the start sector is less than or equal to the end sector, we just return the range [start, end]
            return list(range(start, end + 1))
        else:
            # If the start sector is greater than the end sector, we visit from [start, n] and [1, end]
            # By using sorted(), we ensure the sectors are returned in ascending order, as required
            return sorted(list(range(start, n + 1)) + list(range(1, end + 1)))
