class Solution:
    def pivotInteger(self, n: int) -> int:
        # left = 0
        # right = 0
        # for i in range(1, n + 1):
        #     left += i
        #     right = sum(j for j in range(i, n + 1))
        #     if left == right:
        #         return i
        # return -1
        
        # Math logic alternative
        totalSum=n*(n+1)//2
        curr= round(math.sqrt(totalSum))
        
        if curr*curr==totalSum:
            return curr
         
        return -1
