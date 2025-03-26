test_cases = int(input())

for _ in range(test_cases):
    n = int(input())
    arr = list(map(int, input().split()))

    flag = "NO"

    j = 1
    while j < n:
        if max(arr[0:j]) > min(arr[j:]):
            flag = "YES"
            break
        j += 1
    
    print(flag)