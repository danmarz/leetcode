class Solution:
    def arraySign(self, nums: List[int]) -> int:
        # Optimal solution, without even computing the product
        def signFunc(x):
            return 1 if x > 0 else -1 if x < 0 else 0

        negative_count = 0
        for num in nums:
            if num == 0:
                return 0  # Early exit based on multiplication properties
            elif num < 0:
                negative_count += 1

        # If the count of negatives is odd, return -1; if even, return 1
        return -1 if negative_count % 2 != 0 else 1

        # # Beginner's approach:
        # def signFunc(x):
        #     if x > 0:
        #         return 1
        #     elif x < 0:
        #         return -1
        #     else:
        #         return 0

        # # Calculate product
        # product = 1
        # for num in nums:
        #     product *= num

        # # Return the sign of the product
        # return signFunc(product)
