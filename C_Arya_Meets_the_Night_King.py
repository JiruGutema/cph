# # test_cases = int(input())
# test_cases = 1

# for _ in range((test_cases)):
#     s, b = list(map(int, input().split()))
#     a = list(map(int, input().split()))
#     ans = [0]*(s)
#     for i in range(b):
#         d, g = list(map(int, input().split()))
#         for i in range(s):
#             if a[i] >= d:
#                 ans[i] += g

#     print(*ans)




# test_cases = int(input())

test_cases = 1

for _ in range((test_cases)):
    s, b = list(map(int, input().split()))
    a = list(map(int, input().split()))
    ans = [0] * s
    events = []
    for _ in range(b):
        d, g = list(map(int, input().split()))
        events.append((d, g))
    
    a_sorted = sorted((val, idx) for idx, val in enumerate(a))
    events.sort()
    
    
    j = 0
    total_g = 0
    for d, g in events:
        while j < s and a_sorted[j][0] < d:
            ans[a_sorted[j][1]] = total_g
            j += 1
        total_g += g
    
    while j < s:
        ans[a_sorted[j][1]] = total_g
        j += 1
    
    print(*ans)
