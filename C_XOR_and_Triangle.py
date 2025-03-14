def find_y(x):
    y = x ^ 1
    if y < x:
        a, b, c = x, y, x ^ y
        if a + b > c and a + c > b and b + c > a:
            return y
    return -1

t = int(input())
for _ in range(t):
    x = int(input())
    result = find_y(x)
    print(result)