class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # Count occurrences of each number in the input array
        c = Counter(nums)

        # Count occurrences of numbers in the range [1, len(nums)]
        b = Counter(range(1, len(nums) + 1))

        # Calculate the duplicate and missing numbers
        duplicate = list((c - b).keys())[0]
        missing = list((b - c).keys())[0]

        return [duplicate, missing]

        """ More succint:
        def findErrorNums(self, nums: List[int]) -> List[int]:
            c = Counter(nums)
            b = Counter(range(1, len(nums)+1))
            
            return list((c-b).keys()) + list((b-c).keys())
        """
