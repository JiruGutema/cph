from collections import deque

test_cases = int(input())

for _ in range(test_cases):
    n = int(input())
    nums = list(map(int, input().split()))
    
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]

    # flag = True
    # for i in range(n):
    #     # for j in range(i+1, n+1):
    #     #     if max(nums[i:j]) >= sum(nums[i:j]):
                
    #     stack = []
    #     for j in range(i, n):
    #         while stack and nums[stack[-1]] <= nums[j]:
    #             stack.pop()
    #         stack.append(j)
            
    #         subarray_sum = prefix[j + 1] - prefix[i]
    #         subarray_max = nums[stack[0]]
            
    #         if subarray_max < subarray_sum:
    #             flag =  False
    #             break
    #     if not flag:
    #         break
    # if flag:
    #     print("YES")
    # else:
    #     print("NO")

    

