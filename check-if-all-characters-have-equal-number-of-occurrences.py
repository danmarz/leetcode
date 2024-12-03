class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        # counter = {}
        # for c in s:
        #     if c not in counter:
        #         counter[c] = 1
        #     else:
        #         counter[c] += 1
        # sample = list(counter.values())[0]
        # return all(value == sample for value in counter.values()) if counter.values() else True

        # Optimized approach using set()
        # Step 1: Count character frequencies
        freq_counter = Counter(s)

        # Step 2: Extract unique frequencies
        frequencies = set(freq_counter.values())

        # Step 3: A string is "good" if all frequencies are the same (1 unique frequency)
        return len(frequencies) == 1
