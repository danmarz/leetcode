class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        ## Best solution because it leverages a custom sorting function in the sorted() call:
        # Step 1: Count the frequency of each number in the array using Counter
        freq = Counter(nums)

        # Step 2: Sort the array based on two criteria:
        # First, by frequency in ascending order (key= lambda x: (freq[x], -x) ensures this)
        # Second, if two numbers have the same frequency, sort them in descending order of value (negative sign to reverse order)
        sorted_nums = sorted(nums, key=lambda x: (freq[x], -x))

        return sorted_nums

        # ### Alternative solution:
        # # Count the frequency of each element in the array
        # counter = Counter(nums)
        # print(counter.items())

        # # Sort based on frequency ascending and value descending, without reverse
        # count = sorted(counter.items(), key=lambda x: (x[1], -x[0]))
        # print(count)

        # # Build the result directly
        # ans = []
        # for pair in count:
        #     ans.extend([pair[0]] * pair[1])  # This adds the element 'pair[0]' 'pair[1]' times

        # return ans

        ### Equivalent:
        # counter = Counter(nums)
        # count = sorted(counter.items(), key=lambda x: (x[1], -x[0]))
        # ans = []

        # for pair in count:
        #     for _ in range(0, pair[1]):
        #         ans.append(pair[0])

        # return ans
