n,tot = list(map(int, input().split()))
arr = list(map(int, input().split()))

n = len(arr)
ans = 0
Window = float("inf")
left = 0 

for right in range(n):
    Window += arr[right]

    while Window > tot:
        Window -= arr[left]
        left += 1  
        
    ans += right-left+1

print(ans)


    
    
        

