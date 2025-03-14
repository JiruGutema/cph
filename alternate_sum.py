test_cases = int(input())

for _ in range(test_cases):
    n = int(input())
    arr = list(map(int, input().split()))

    flag = arr[0] > 0
    tot = 0
    curr = arr[0]

    for i in range(1, len(arr)):
        if (flag and arr[i] > 0) or (not flag and arr[i] < 0):
            curr = max(curr, arr[i])
        else:
            tot += curr 
            curr = arr[i]
            flag = not flag  

    tot += curr  
    print(tot)

