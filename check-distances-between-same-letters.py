class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        # n = len(s)
        # char_distances = defaultdict(str)

        # for i in range(n):
        #     if s[i] not in char_distances:
        #         char_distances[s[i]] = [ i ]
        #     else:
        #         char_distances[s[i]] += [ i ]

        # for char, distances in char_distances.items():
        #     first, second = distances
        #     current_distance = 0

        #     for d in range(first, second - 1):
        #         current_distance += 1
        #     if current_distance != distance[ord(char) - ord('a')]:
        #         return False

        # return True

        # Same logic structure, but using an optimized approach:
        positions = {}  # Dictionary to store first occurrence index of each character

        for i, char in enumerate(s):
            char_index = ord(char) - ord("a")  # Convert character to index (0-25)

            if char in positions:  # Second occurrence
                actual_distance = (
                    i - positions[char] - 1
                )  # Compute distance between occurrences
                if actual_distance != distance[char_index]:
                    return False  # If mismatch, return False
            else:
                positions[char] = i  # Store first occurrence index

        return True  # If all checks pass, return True
