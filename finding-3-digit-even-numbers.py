class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        count_digits = Counter(digits)
        nums = [num for num in range(100, 1000) if num % 2 == 0]
        nums = [list(str(digit)) for digit in nums]
        even_nums = []

        for num in nums:
            count_num = Counter([int(n) for n in num])
            complete = True
            for key in count_num.keys():
                if key not in count_digits or count_digits[key] < count_num[key]:
                    complete = False
                    break
            if complete:
                even_nums.append(num)

        return [int("".join(num)) for num in even_nums]


# # Alternative using itertools.permutations for a more streamlined approach
# from collections import Counter
# from itertools import permutations
# from typing import List

# class Solution:
# def findEvenNumbers(self, digits: List[int]) -> List[int]:
# # Use a set to ensure unique integers
# unique_numbers = set()

# # Iterate over all permutations of 3 digits
# for perm in permutations(digits, 3):
#     # Form the number and check constraints
#     if perm[0] != 0 and perm[2] % 2 == 0:  # No leading zero and even number
#         num = perm[0] * 100 + perm[1] * 10 + perm[2]
#         unique_numbers.add(num)

# # Return the sorted list of unique integers
# return sorted(unique_numbers)
