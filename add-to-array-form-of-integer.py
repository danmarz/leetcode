class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        result = []
        carry = 0
        i = len(num) - 1

        while i >= 0 or k > 0:
            if i >= 0:
                carry += num[i]
            if k > 0:
                carry += k % 10
                k //= 10

            # Append the least significant digit to result
            result.append(carry % 10)
            carry //= 10
            i -= 1

        # If there's any remaining carry, add it to the result
        if carry:
            result.append(carry)

        # Reverse the result since we appended digits from right to left
        return result[::-1]
