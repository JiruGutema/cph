
n, t, c = map(int, input().split())
crime_severities = list(map(int, input().split()))
count = 0
valid_segments = 0
for i in range(n):
    if crime_severities[i] <= t:
        count += 1
    else:
        count = 0
    
    if count >= c:
        valid_segments += 1

print(valid_segments) 