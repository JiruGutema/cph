test_cases = int(input())
for _ in range(test_cases):
    n = int(input())
    nums = list(map(int, input().split()))
    
    current = 1
    for num in nums:
        if current == num:
            current += 1
        current += 1
    print(current-1)
