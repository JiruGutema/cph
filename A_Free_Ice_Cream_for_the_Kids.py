n, m = list(map(int, input().split()))
count = 0
icecream = m

for _ in range(n):
    a, b = list(map(str, input().split()))
    b = int(b)
    if a == "-":
        if b > icecream:
            count += 1
        else:
            icecream -= b
    else:
        icecream += b
print(icecream, count)

