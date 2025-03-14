n,s = list(map(int, input().split()))


count = 0
curr = 0

# while curr < s:

#     if s - curr >= n:
#         curr += n
#     else:
#         curr += s - curr
#     count += 1

while curr +n < s:
    curr += n
    count += 1
if curr < s:
    count += 1


print(count)


