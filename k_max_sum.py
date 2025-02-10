prefix = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    row_sum = 0
    for j in range(1, m + 1):
        row_sum += matrix[i - 1][j - 1]
        prefix[i][j] = prefix[i - 1][j] + row_sum
max_mum = 0


for i in range(k,n+1):
    for j in range(k,m+1):
        total = prefix[i][j] - prefix[i-k][j] - prefix[i][j-k] + prefix[i-k][j-k]
        max_mum = max(max_mum,total)
