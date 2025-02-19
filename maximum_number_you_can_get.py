class Solution:
    def maxCoins(self, piles):
        piles.sort()
        count = 0

        i = 1
        while i < len(piles):
            count += piles[i]
            i += 3
        return count
solution = Solution()
solution.maxCoins([9,8,7,6,5,1,2,3,4])