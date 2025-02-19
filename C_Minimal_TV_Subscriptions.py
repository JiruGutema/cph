test_cases = int(input())

for _ in range(test_cases):
    n, k, d = list(map(int, input().split()))
    show = list(map(int, input().split()))

    i = 0
    j = d
    small = d
    
    while j <= n:
        small = min(small, len(set(show[i:j])))
        i += 1
        j += 1
    print(small)





test_cases = int(input())

for _ in range(test_cases):
    n, k, d = list(map(int, input().split()))
    show = list(map(int, input().split()))

    freq = {}
    for i in range(d):
        if show[i] in freq:
            freq[show[i]] += 1
        else:
            freq[show[i]] = 1

    small = len(freq)

    for i in range(d, n):
        if freq[show[i - d]] == 1:
            del freq[show[i - d]]
        else:
            freq[show[i - d]] -= 1

        if show[i] in freq:
            freq[show[i]] += 1
        else:
            freq[show[i]] = 1

        small = min(small, len(freq))

    print(small)

