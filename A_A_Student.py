from collections import Counter
test_cases = int(input())

for _ in range(test_cases):
    a, b, c = map(int, input().split())
    max_score = max(a, b, c)
    min_additional_points = []
    count = Counter((a, b, c))[max_score]
   
    for score in (a, b, c):
        if score == max_score and count == 1:
            min_additional_points.append(0)
        else:
            min_additional_points.append(max_score - score + 1)
    print(*min_additional_points)