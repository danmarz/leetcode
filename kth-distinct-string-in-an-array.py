class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        # # Non-optimal approach using two lists:
        # distinct = []
        # non_distinct = []
        # for string in arr:
        #     if string not in distinct and string not in non_distinct:
        #         distinct.append(string)
        #     else:
        #         if string in distinct:
        #             distinct.remove(string)
        #             non_distinct.append(string)
        # # print(distinct)
        # if not distinct or len(distinct) < k:
        #     return ""
        # else:
        #     return distinct[k - 1]

        # # A better way, O(1) using a dictionary
        # Count occurrences of each string
        count = Counter(arr)

        # Collect distinct strings in order of appearance
        distinct = [string for string in arr if count[string] == 1]

        # Return the kth distinct string if it exists, else ""
        return distinct[k - 1] if k <= len(distinct) else ""
