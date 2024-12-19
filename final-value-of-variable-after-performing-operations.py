class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        # # Dictionary approach
        # mods = {"++X": 1, "X++": 1, "--X": -1, "X--": -1}
        # x = 0
        # for operation in operations:
        #     x += mods[operation]
        # return x

        # Check sign in string alternative
        X = 0
        for op in operations:
            # Check if operation is an increment
            if "+" in op:
                X += 1
            else:
                # Otherwise it must be a decrement operation
                X -= 1
        return X
