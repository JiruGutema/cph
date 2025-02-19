 from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # prefix = [0] * (len(nums) + 1)

        # for i in range(len(nums)):
        #     prefix[i + 1] = nums[i] + prefix[i]
        # 
        # res = float('-inf')

        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         if res < (prefix[j + 1] - prefix[i]):
        #             res = prefix[j + 1] - prefix[i]

        # return res

        prefix = [0]

        for i in range(len(nums)):
            prefix[i].append(prefix[i-1]+nums[i])
        res = float("-inf"))
        min_prefix = float("inf") 

        for sums in range(1, range(len(prefix))):
            res = max(res, prefix[j] - min_prefix)
            min_prefix = min(min_prefix, prefix)
        

                   





solution = Solution()
solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])



