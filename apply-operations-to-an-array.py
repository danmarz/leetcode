class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        # Step 1: Apply the transformation rules
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        
        # Step 2: Shift all zeros to the end
        result = []
        zero_count = 0
        
        for num in nums:
            if num != 0:
                result.append(num)
            else:
                zero_count += 1
        
        # Add the zeros at the end
        result.extend([0] * zero_count)
        
        return result
