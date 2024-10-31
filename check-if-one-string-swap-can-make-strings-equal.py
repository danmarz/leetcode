class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # Early exit if strings are already equal, no swap is needed.
        if s1 == s2:
            return True

        # Collect mismatched positions directly as a list of indices.
        mismatches = [i for i, (a, b) in enumerate(zip(s1, s2)) if a != b]

        # Check for the condition: exactly two mismatches, and they can be swapped.
        return (
            len(mismatches) == 2
            and s1[mismatches[0]] == s2[mismatches[1]]
            and s1[mismatches[1]] == s2[mismatches[0]]
        )

        # if s1 == s2:
        #     return True

        # s2_arr = [ _ for _ in s2 ]
        # num_diff = 0
        # diff_pos = []

        # for pos, char in enumerate(s2_arr):
        #     if char != s1[pos]:
        #         num_diff += 1
        #         if num_diff > 2:
        #             return False
        #         diff_pos.append(pos)

        # if num_diff != 2:
        #     return False
        # else:
        #     temp = s2_arr[diff_pos[0]]
        #     s2_arr[diff_pos[0]] = s2_arr[diff_pos[1]]
        #     s2_arr[diff_pos[1]] = temp

        # return s1 == "".join(s2_arr)
