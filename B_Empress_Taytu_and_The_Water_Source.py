


t = int(input())
results = []
for _ in range(t):
    n, k = map(int, input().split())
    d = list(map(int, input().split()))
    a = list(map(int, input().split()))
    left, right = 1, max(d)
    answer = -1
    while left <= right:
        mid = (left + right) // 2
        total_time = 0
        for i in range(n):
            trips = (d[i] + mid - 1) // mid
            total_time += trips * a[i]
            
        if total_time <= k:
            answer = mid

            right = mid - 1
        else:
            left = mid + 1

    results.append(answer)

for res in results:
    print(res)


