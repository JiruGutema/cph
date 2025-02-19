n,tot = list(map(int, input().split()))
arr = list(map(int, input().split()))

n = len(arr)
ans = float("inf")
Window = 0
left = 0 

for right in range(n):
    Window += arr[right]

    while Window >= tot:
        Window -= arr[left]
        ans = min(ans, right-left+1)
        left += 1

print(ans) if ans != float("inf") else print(-1)


    
    
        

