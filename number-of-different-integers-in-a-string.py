class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        nums_set = set()
        num_to_compare = ""

        for char in word:
            if char.isnumeric():
                num_to_compare += char
            elif (
                num_to_compare
            ):  # If a non-digit is encountered and num_to_compare is not empty
                nums_set.add(int(num_to_compare))
                num_to_compare = ""

        # Final check in case the last character in word was part of a number
        if num_to_compare:
            nums_set.add(int(num_to_compare))

        return len(nums_set)
