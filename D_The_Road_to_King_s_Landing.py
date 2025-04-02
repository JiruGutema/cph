test_cases = int(input())
for _ in range(test_cases):
    seg = int(input())
    intervals = []
    curr_k = float("-inf")
    curr_min = float("inf")
    pre = 0
    for i in range(seg):

        l, r = list(map(int, input().split()))
        if not intervals:
            intervals.append((l, r))
        else:
            intervals.append((l, r))

    for i in intervals:
        curr_k = max((pre - i[0]), curr_k )

        pre = i[0]
    print(curr_k)



    

