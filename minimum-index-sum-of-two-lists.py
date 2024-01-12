from collections import defaultdict


def findRestaurant(list1, list2):
    # Create a dictionary to store the index sum for each common string
    index_sum_dict = defaultdict(int)

    # Populate the dictionary with index sums for common strings
    for i, restaurant in enumerate(list1):
        if restaurant in list2:
            # Calculate the index sum and store it in the dictionary
            index_sum_dict[restaurant] = i + list2.index(restaurant)

    # Find the minimum index sum among common strings
    min_index_sum = min(index_sum_dict.values())

    # Return the list of common strings with the minimum index sum
    return [
        restaurant
        for restaurant, index_sum in index_sum_dict.items()
        if index_sum == min_index_sum
    ]
