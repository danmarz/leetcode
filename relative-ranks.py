class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # Sort the scores in descending order
        sorted_scores = sorted(score, reverse=True)

        # Create a dictionary to map each score to its rank as a string
        rank_dict = {score: str(i + 1) for i, score in enumerate(sorted_scores)}

        # Define medal ranks
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]

        # Store the ranks of each athlete
        result = []

        # Iterate through each score in the original score list
        for s in score:
            # If the rank is within top 3, append the corresponding medal
            if rank_dict[s] in {"1", "2", "3"}:
                result.append(medals[int(rank_dict[s]) - 1])
            # Otherwise, append the numerical rank
            else:
                result.append(rank_dict[s])

        return result
