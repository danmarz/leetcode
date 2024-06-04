class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        # Using list.extend() method:
        decompressed_list = []

        # Iterate over the list in steps of 2 to get pairs of [freq, val]
        for i in range(0, len(nums), 2):
            freq = nums[i]
            val = nums[i + 1]

            # Extend the decompressed_list by freq occurrences of val
            decompressed_list.extend([val] * freq)

        return decompressed_list

        """ Alternative using a helper function to chunk-divide nums into pairs:
        def divide_chunks(l, n):    
        # looping till length l 
            for i in range(0, len(l), n):  
                yield l[i:i + n]

        ans = []
        x = list(divide_chunks(nums, 2)) 

        for pair in x:
            decompressed = [ pair[1] for _ in range(pair[0]) ]
            ans += decompressed
        
        return ans
        """
