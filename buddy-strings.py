class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        if s == goal:
            # Check if s has duplicate characters
            return len(set(s)) < len(s)

        diff = [(a, b) for a, b in zip(s, goal) if a != b]

        # print(diff)

        # Two strings can only be made equal by swapping two letters if there are exactly two differences
        return len(diff) == 2 and diff[0] == diff[1][::-1]
