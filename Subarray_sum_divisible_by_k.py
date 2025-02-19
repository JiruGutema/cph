class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        dictionary = Counter()
        nums = [0] + nums
        count = 0 

        for i in range(1, len(nums)):
            nums[i] += nums[i-1]

        for i in range(len(nums)):
            curr_element = nums[i] - k
            
            if curr_element in dictionary.keys() and curr_element%k == 0:
                count += dictionary[curr_element]
            dictionary[nums[i]] += 1
            
        return (count)

    
solution = Solution()
solution.subarraysDivByK([4,5,0,-2,-3,1], 5)

