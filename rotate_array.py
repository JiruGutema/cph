nums = [1, 2, 3, 4, 5, 6, 7]
k = 3

i = 0
j = len(nums) - 1
while i < j:
    nums[i], nums[j] = nums[j], nums[i]
    i += 1
    j -= 1

start = 0
end = k - 1
while start < end:
    nums[start], nums[end] = nums[end], nums[start]
    start += 1
    end -= 1

start = k
end = len(nums) - 1
while start < end:
    nums[start], nums[end] = nums[end], nums[start]
    start += 1
    end -= 1

print(nums)