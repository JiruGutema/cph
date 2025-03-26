def is_beautiful(n, p):
    pos = {value: index for index, value in enumerate(p)}  
    left, right = n, -1
    result = []

    for m in range(1, n + 1):
        index = pos[m] 
        
        left = min(left, index)
        right = max(right, index)
        
        result.append('1' if right - left + 1 == m else '0')

    return ''.join(result)

t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    print(is_beautiful(n, p))
