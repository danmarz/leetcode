class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = 0
        while n > 1:
            if n % 2 == 0:  # handle even case
                n //= 2  # divide teams by 2, because n is even
                matches += n  # the number of matches is exactly n/2
            else:  # handle odd case
                n //= 2  # floor division: one team advances
                matches += n + 1  # add the advanced team to the match count
        return matches
