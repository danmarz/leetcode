def removeDuplicates(nums):
    # refactored
    nums[:] = sorted(set(nums))
    return len(nums)

    """
    if not nums:
        return 0

    slow = 0

    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]

    return slow + 1
    """
