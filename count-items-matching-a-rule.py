class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        # Create a mapping from rule keys to their corresponding index in the item lists
        index_map = {"type": 0, "color": 1, "name": 2}

        # Retrieve the index corresponding to the given ruleKey
        idx = index_map[ruleKey]

        # Use a generator expression to count the number of items that match the rule
        return sum(1 for item in items if item[idx] == ruleValue)

        # # Novice approach, more verbose & less efficient
        # matches = 0

        # for item in items:
        #     itemType, itemColor, itemName = item

        #     if ruleKey == "type" and ruleValue == itemType:
        #         matches += 1
        #     elif ruleKey == "color" and ruleValue == itemColor:
        #         matches += 1
        #     elif ruleKey == "name" and ruleValue == itemName:
        #         matches += 1

        # return matches
