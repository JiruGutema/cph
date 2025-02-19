n,total = list(map(int, input().split()))
arr = list(map(int, input().split()))

current_sum = 0
current_length = 0
left = 0

for right in range(n):
    current_sum += arr[right]
    while current_sum >= total:
        current_sum -= arr[left]
        current_length +=n-right
        left +=1
    
print(current_length)

