n,m, k = list(map(int, input().split()))

i = 0

while i < k:
    if i%2 == 0:
        n -= 1
    else:
        m -= 1
    i += 1
print(n*m)