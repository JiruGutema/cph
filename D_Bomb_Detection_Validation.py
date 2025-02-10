n, m = map(int, input().split())
flag = True
grid = []
for i in range(n):
    row = input()
    grid.append(row)

for row in range(n):
    for col in range(m):
        if grid[row][col] == "*":
            continue
        count = 0

        if 0 <= col-1 < m and grid[row][col-1] == "*":
            count += 1
        if 0 <= col+1 < m and grid[row][col+1] == "*":
            count += 1

        if 0 <= row-1 < n and grid[row-1][col] == "*":
            count += 1
        if 0 <= row+1 < n and grid[row+1][col] == "*":
            count += 1
            
        if 0 <= col-1 < m and 0 <= row+1 < n and grid[row+1][col-1] == "*":
            count += 1
        if 0 <= col-1 < m and 0 <= row-1 < n and grid[row-1][col-1] == "*":
            count += 1
        
        if 0 <= col+1 < m and 0 <= row+1 < n and grid[row+1][col+1] == "*":
            count += 1
        if 0 <= col+1 < m and 0 <= row-1 < n and grid[row-1][col+1] == "*":
            count += 1

        if count != 0 and  grid[row][col] == ".":
            flag = False
        elif grid[row][col] != "." and int(grid[row][col]) != count:
            flag = False

if flag:
    print("YES")
else:
    print("NO")

