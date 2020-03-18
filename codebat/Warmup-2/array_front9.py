def array_front9(nums):
    # First figure the end for the loop
    end = len(nums)
    if end > 4:
        end = 4

    for i in range(end):
        if nums[i] == 9:
            return True
    return False