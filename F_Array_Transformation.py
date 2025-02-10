from collections import Counter


tests = int(input())
for _ in range(tests):
    n = int(input())
    nums = list(map(int, input().split()))
    # print(nums)

    count = Counter(nums)
    # print(count)
    repetition = max(list(v for v in count.values()))
    # print(repetition)

    nums_operation_needed = 0
    for v in count.values():
        nums_operation_needed += abs(2-v)
    
    print(nums_operation_needed)

    