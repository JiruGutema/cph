k = int(input())
for _ in range(k):
    n,m = map(int,input().split())
    mat = [list(map(int,input().split())) for _ in range(n)]
    directions = [(1,1),(-1,-1),(1,-1),(-1,1)]

    def helper(r,c):
        if 0 <= r < n and 0 <= c < m:
            return True
        else:
            return False
    
    ans = 0
    for r in range(n):
        curr_count = 0
        for c in range(m):
            curr_count += mat[r][c]




            
            


































































# def inbound(x,y):
#         if 0<=x<n and 0<= y <m:
#             return True
#         return False
#     res = []
#     for i in range(n):
#         for j in range(m):
#             el_sum = -3*mat[i][j]
#             for dx,dy in directions:
#                 t ,s = i,j
#                 while inbound(t,s):
#                     el_sum += mat[t][s]
#                     t,s = t+dx,s+dy
#             res.append(el_sum)