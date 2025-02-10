
n = int(input())
mat = [list(map(int,input().split())) for _ in range(n)]
res = 0
for i in range(n):
    res += mat[i][i] + mat[i][n-i-1] + mat[n//2][i] + mat[i][n//2]
    # mat i i for main diagonal
    # i n-i-1 for secondary diagonal
    # n//2 i for middle row
    # i n//2 for middle col

res -= 3*mat[n//2][n//2]
# we are substracting because of the we added middle element three times
print(res)
