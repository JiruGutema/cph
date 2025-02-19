n = int(input())
nums = map(int, input().split())

min_num = min(abs(num) for num in nums ) 
print(abs(min_num))

diff = 0
for num in nums:
    diff += abs(num)
    if num < 0:
        diff -= 2*min_num
print(diff)

print(name)name in the 
