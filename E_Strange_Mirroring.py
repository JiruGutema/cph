
def is_beautiful(n, p):
    min_pos = n + 1
    max_pos = 0
    result = []
    for m in range(1, n + 1):
        pos = p.index(m)
        min_pos = min(min_pos, pos)
        max_pos = max(max_pos, pos)
        if max_pos - min_pos + 1 == m:
            result.append('1')
        else:
            result.append('0')
    return ''.join(result)

t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    print(is_beautiful(n, p))