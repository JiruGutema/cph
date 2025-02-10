n = int(input())
nums = map(int, input().split())

min_num = min(abs(num) for num in nums ) 
print(abs(min_num))