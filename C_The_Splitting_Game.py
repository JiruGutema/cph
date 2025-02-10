
# time limit exceed

times = int(input())
for _ in range(times):
    n = int(input())
    s = input()
    string1 = set()
    string2 = set()
    max_total = 0
    for i in range(n):
        current = len(set(s[:i])) + len(set(s[i:]))
        max_total = max(max_total, current)
    print(max_total)


# same operation with different
for _ in range(times):
    n = int(input())
    s = input()

    forward_sum = [0] * n
    backward_sum = [0] * n
    forward = set()
    backward = set()


    for i in range(n):
        forward.add(s[i])
        forward_sum[i] = len(forward)


    for i in range(n - 1, -1, -1):
        backward.add(s[i])
        backward_sum[i] = len(backward)

    max_total = 0
    for i in range(n - 1):
        max_total = max(max_total, forward_sum[i] + backward_sum[i + 1])
    # print(forward_sum)
    # print(backward_sum)
    print(max_total)


        
