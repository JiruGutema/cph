import math
def sort(nums):
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums


def bucket_sort(nums):
    bucket = math.ceil(len(nums)**0.5)
    minn = min(nums)
    maxx = max(nums)

    bucket_range = (maxx - minn)/bucket
    buckets = [[] for _ in range(bucket)]

    for num in nums:
        index = int((num - minn)/bucket_range)
        if index == bucket:
            index -= 1
        buckets[index].append(num)
    sorted_arr = []
    for bucket in buckets:
        sorted_bucket = (sort(bucket))
        sorted_arr.extend(sorted_bucket)
    print(sorted_arr)

bucket_sort([1,2,3,4,6,5,4,3])
        

    

    

