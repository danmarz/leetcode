class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # Initialize variables to store the result and carry.
        result = []
        carry = 0
        
        # Convert input strings to lists of integers in reverse order.
        num1 = [int(char) for char in num1[::-1]]
        num2 = [int(char) for char in num2[::-1]

        # Make the two lists equal in length by adding leading zeros.
        mx = max(len(num1), len(num2))
        num1 += [0] * (mx - len(num1))
        num2 += [0] * (mx - len(num2)

        for i in range(mx):
            total = num1[i] + num2[i] + carry
            digit = total % 10
            carry = total // 10
            result.append(str(digit))

        if carry:
            result.append(str(carry))
        
        # Reverse the result and join the digits to create the final string.
        return ''.join(result[::-1]