from collections import Counter
class Solution:
    def maxScore(self, s: str) -> int:

        length = len(s)
        counter = Counter(s)
        ones = counter["1"]
        zeros = 0

        ans = 0 

        for i in range(length):
            if s[i] == '1':
                ones -= 1
                 
            else:
                zeros += 1


            ans = max(zeros + ones, ans)
        return ans  

solution = Solution()
print(solution.maxScore("011101")) # 5

