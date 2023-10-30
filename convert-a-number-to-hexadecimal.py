class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"  # Special case for zero.

        if num < 0:
            num += 2**32  # Convert negative integer to its two's complement.
            # num = (1 << 32) + num  # Alternative

        hex_digits = "0123456789abcdef"
        result = []

        while num > 0:
            remainder = num % 16
            result.append(hex_digits[remainder])
            num //= 16

        return "".join(result[::-1])

        """ Alternatively, format & return the result as a string from the get-go
        
        # Initialize an empty string to store the hexadecimal representation of the input number
        hex_num = ''  

        # Repeatedly divide the input number by 16 and convert the remainder to its corresponding hexadecimal digit until the quotient becomes zero
        while num > 0:
        # Get the remainder of dividing the input number by 16
            digit = num % 16  
        # Convert the remainder to its corresponding hexadecimal digit
            hex_digit = hex_digits[digit]  
        # Add the hexadecimal digit to the beginning of the hexadecimal representation
            hex_num = hex_digit + hex_num  
        # Update the input number by dividing it by 16
            num //= 16  
        
        return hex_num
        """
