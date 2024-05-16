class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return len(set(Counter(arr).values())) == len(set(arr))

        """ Better solution w/o using Counter
        d = {}
        for n in arr:
            d[n] = d.get(n, 0) + 1

        return len(d) == len(set(d.values()))
        """

        """ Bruteforce
        num_count = {}

        for num in arr:
            num_count[num] = arr.count(num)

        values = list(num_count.values())
        values.sort()
        values_set = set(num_count.values())
        values_set_list = list(values_set)
        values_set_list.sort()

        return values == values_set_list
        """
