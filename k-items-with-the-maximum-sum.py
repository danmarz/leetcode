class Solution:
    def kItemsWithMaximumSum(
        self, numOnes: int, numZeros: int, numNegOnes: int, k: int
    ) -> int:
        # sum_k = 0
        # for i in range(k):
        #     if numOnes:
        #         sum_k += 1
        #         numOnes -= 1
        #         continue
        #     if numZeros:
        #         numZeros -= 1
        #         continue
        #     if numNegOnes:
        #         sum_k -= 1
        #         numNegOnes -= 1
        #         continue
        # return sum_k

        # Optimized O(1) solution
        # Pick as many 1s as we can, up to k
        ones_taken = min(numOnes, k)
        k -= ones_taken

        # Zeros don't affect the sum, just reduce the count of k
        zeros_taken = min(numZeros, k)
        k -= zeros_taken

        # The rest must be -1s, each reduces the sum
        neg_ones_taken = k

        return ones_taken - neg_ones_taken
