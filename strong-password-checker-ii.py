class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        # if len(password) < 8:
        #     return False
        # if not any(char.isupper() for char in password) or not any(char.islower() for char in password) or not any(char.isdigit() for char in password):
        #     return False
        # if not any(char in "!@#$%^&*()-+" for char in password):
        #     return False
        # for i in range(1, len(password)):
        #     if password[i] == password[i - 1]:
        #         return False
        # return True

        # Elegant solution: one pass, with flags
        if len(password) < 8:
            return False

        has_lower = has_upper = has_digit = has_special = False
        special_chars = set("!@#$%^&*()-+")

        for i, char in enumerate(password):
            # Check for adjacent duplicate
            if i > 0 and password[i] == password[i - 1]:
                return False

            # Check character categories
            if char.islower():
                has_lower = True
            elif char.isupper():
                has_upper = True
            elif char.isdigit():
                has_digit = True
            elif char in special_chars:
                has_special = True

        # Ensure all conditions are met
        return has_lower and has_upper and has_digit and has_special
