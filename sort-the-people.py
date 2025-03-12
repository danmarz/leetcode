class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # sorted_heights = sorted(heights, reverse=True)
        # res = []
        # for height in sorted_heights:
        #     res.append(names[heights.index(height)])
        # return res

        # Optimized solution:
        # Pair each name with the corresponding height
        paired_list = list(zip(names, heights))

        # Sort the list of tuples by height in descending order
        paired_list.sort(key=lambda x: x[1], reverse=True)

        # Extract the sorted names into a new list
        sorted_names = [name for name, _ in paired_list]

        return sorted_names
