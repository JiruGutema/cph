test_cases = int(input())

for _ in range(test_cases):
    n, k = list(map(int, input().split()))
    weather = [(val, idx) for idx, val in enumerate(map(int, input().split()))]
    temperature = list(map(int, input().split()))

    weather_s = sorted(weather, key=lambda x: x[0])
    temperature.sort()

    ans = [0] * n
    for i in range(n):
        ans[weather_s[i][1]] = temperature[i]

    ans = [ans[idx] for val, idx in weather]
    print(*ans)



