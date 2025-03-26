def permutations(arr):
    if sorted(arr) == list(range(1, len(arr) + 1)):
        return 1
    else:
        return 0

test_cases = int(input())

for _ in range(test_cases):
    n = int(input())
    arr = list(map(int, input().split()))
    for num in range(1, n + 1):
        i = 0
        j = num
        ans = 0
        while j <= n:
            if permutations(arr[i:j]):
                ans = 1
                break
            j += 1
            i += 1
        print(ans, end="")
    print()




test_cases = int(input())

# Loop through each test case
for _ in range(test_cases):

    n = int(input())

    p = list(map(int, input().split()))
    

    position = [0] * (n + 1)
    for i in range(n):
        position[p[i]] = i
    print(position)
    

    min_left = n
    max_right = -1

    result = []
    

    for m in range(1, n + 1):
    
        min_left = min(min_left, position[m])
        max_right = max(max_right, position[m])
        
    
        if max_right - min_left + 1 == m:
            result.append(1)
        else:
            result.append(0)
    

    print("".join(map(str, result)))
