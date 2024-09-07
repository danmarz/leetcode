class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        # Iterate over each possible starting index i
        # The range stops at len(arr) - m * k + 1 to avoid going out of bounds
        for i in range(len(arr) - m * k + 1):
            # Assume initially that the pattern repeats k times
            match = True
            # Check the next k-1 patterns to see if they match the first one
            for j in range(1, k):
                # Compare the current pattern (arr[i:i+m]) with the next pattern (arr[i+j*m:i+j*m+m])
                if arr[i : i + m] != arr[i + j * m : i + j * m + m]:
                    # If any of the k-1 patterns do not match, set match to False and break
                    match = False
                    break
            # If all k patterns matched, return True
            if match:
                return True
        # If no pattern of length m repeats k times, return False
        return False
