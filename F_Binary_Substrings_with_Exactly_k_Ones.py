

k = int(input())
string = input()

n = len(string)
count_ones = 0
ans = 0
prefix_count = {0: 1}

for char in string:
    if char == "1":
        count_ones += 1
    if count_ones - k in prefix_count:
        ans += prefix_count[count_ones - k]
    if count_ones in prefix_count:
        prefix_count[count_ones] += 1
    else:
        prefix_count[count_ones] = 1

print(ans)
