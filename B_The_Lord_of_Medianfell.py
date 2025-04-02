test_cases = int(input())

for _ in range(test_cases):
    n, s = list(map(int, input().split()))
    if n == 1:
        print(s)
    elif n == 2:
        print(s //2 )
    else:
        print(s // (n // 2 + 1))
