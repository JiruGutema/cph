def cyclic_sort(nums):
    left, right = 0, len(nums) - 1
    while left <= right:
        correct = nums[left] - 1
        if correct != left:
            nums[left], nums[correct] = nums[correct], nums[left]
        else:
            left += 1
    return nums

