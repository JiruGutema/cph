
n,m = map(int,input().split())
mat = [list(map(str, list(input()))) for _ in range(n)]
directions = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
def inbound(x,y):
    if 0 <= x < n-1 and 0 <= y < m-1:
        return True
    return False
res = []
nums = set(str(i) for i in range(1, 9))
return_flag = True
for i in range(n):
    for j in range(m):
        # check for the invalid in the matrix
        flag = True
        # current element for the comparison
        
        
        for dx,dy in directions:
            t ,s = i + dx ,j + dy
            if inbound(t,s):
                current = mat[i][j]
                neighbour = mat[t][s]
                
                # have to skip the current element
                if current != neighbour:
                    if current in nums and neighbour != "*":
                        flag = False
                        break
                    elif current == "." and neighbour == "*":
                        flag = False
                        break

        if not flag:
            return_flag = flag
            break
if return_flag:
    print("YES")
else:
    print("NO")