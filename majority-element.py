class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Sorting approach
        """
        nums.sort()
        n = len(nums)
        return nums[ n // 2 ]
        """

        # Alternative sorting approach
        middle = len(nums) // 2
        return sorted(nums)[middle]

        # Moore voting algorithm approach
        """
        count = 0
        candidate = 0
        
        for num in nums:
            if count == 0:
                candidate = num
            
            if num == candidate:
                count += 1
            else:
                count -= 1
        
        return candidate
        """

        # Brute force :)
        """ 
        seen = set(num for num in nums)
        
        most_seen = 0
        current_count = 0
        
        for num in seen:
            count = nums.count(num)
            if count > current_count:
                current_count = count
                most_seen = num

        return most_seen
        """
