n, m = map(int, input().split())
heights = list(map(int, input().split()))

prefix_f = [0] * n
prefix_r = [0] * n

for i in range(1, n):
    if heights[i - 1] > heights[i]:
        prefix_f[i] = prefix_f[i - 1] + (heights[i - 1] - heights[i])
    else:
        prefix_f[i] = prefix_f[i - 1]

for i in range(n - 2, -1, -1):
    if heights[i + 1] > heights[i]:
        prefix_r[i] = prefix_r[i + 1] + (heights[i + 1] - heights[i])
    else:
        prefix_r[i] = prefix_r[i + 1]

for _ in range(m):
    sj, tj = map(int, input().split())
    sj -= 1
    tj -= 1
    if sj < tj:
        print(prefix_f[tj] - prefix_f[sj])
    else:
        print(prefix_r[tj] - prefix_r[sj])
            

