class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        result = []
        current_num = 0  # Initialize the current number to 0
        for bit in nums:
            current_num = (
                current_num << 1
            ) + bit  # Update current_num with the next bit
            result.append(
                current_num % 5 == 0
            )  # Check if current_num is divisible by 5 and append the result
        return result
