# extra space implementation

def quick_sort_extra(nums):
    if len(nums) <= 1:
        return nums 
    left,pivot, right = partition_extra(nums)

    return quick_sort_extra(left) + [pivot] + quick_sort_extra(right)
    
def partition_extra(nums):
    left = []
    right = []
    pivot = nums[0]

    for num in nums:
        if num <= pivot:
            left.append(num)
        else:
            right.append(num)
    return left, pivot, right
print(quick_sort_extra([1,54,3,2,5,7,7]))

# implementing quick sort inplace

def quick_sort(nums, left, right):
    if left >= right:
        return
    
    pivot_index = partition(nums, left, right)
    quick_sort(nums, left, pivot_index - 1)
    quick_sort(nums, pivot_index + 1, right)

def partition(nums, left, right):
    pivot = left
    holder = left + 1

    for seeker in range(holder, right + 1):
        if nums[seeker] <= nums[pivot]:
            nums[seeker], nums[holder] = nums[holder], nums[seeker]
            holder += 1
    nums[pivot], nums[holder - 1]  = nums[holder - 1], nums[pivot]

    return holder - 1


