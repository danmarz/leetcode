class Solution:
    def minOperations(self, logs: List[str]) -> int:
        # Initialize the depth to 0, representing the main folder
        depth = 0

        # Iterate over each operation in the logs
        for action in logs:
            if "../" in action:  # same as, if log == "../":
                if depth >= 1:  # same as, if depth > 0:
                    depth -= 1
            elif "./" in action:  # same as, elif log == "./":
                # Remain in the same folder; do nothing
                continue
            else:
                # Move to a child folder
                depth += 1

        # The minimum number of operations to go back to the main folder is the current depth
        return depth
