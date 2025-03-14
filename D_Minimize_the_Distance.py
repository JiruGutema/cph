n = int(input())
points = list(map(int, input().split()))


points.sort()
optimal_point = points[(n - 1) // 2]

print(optimal_point)