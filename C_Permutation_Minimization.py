from collections import deque
text_cases = int(input())

for _ in range(text_cases):
    smallest_p = deque()
    n = int(input())
    nums = list(map(int, input().split()))
    for num in nums:
        if not smallest_p:
            smallest_p.append(num)
        else:
            if smallest_p[0] >= num:
                smallest_p.appendleft(num)
            else:
                smallest_p.append(num)
    print(*smallest_p)


