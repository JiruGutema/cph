# The Ethiopian Warrior Colonel Abdisa Aga is captured by fascist forces on the Island of Sicily, Italy. He can't accept succumbing to his enemy and decides to escape from the prison. The prison is a tall tower and his cell is at a height h
#  from the ground. He is planning to jump out of the window, but the window is too far from the ground. Thus, he plans to use blankets he found in the prison and make a long rope by tying them to one another.

# Abdisa wants to know if the rope he made from the blankets is long enough to help him jump out of the window. A rope is long enough if it is greater than or equal to the height h
#  from his window to the ground.

# Given n
#  blankets with varying heights and widths, determine if Abdisa can create a rope long enough to facilitate an escape from the window, using either the height or the width of each blanket. Assume there is a negligible amount of material from the blankets used for tying them together.

# Input
# The first line of the input contains an integer t
#  (1≤t≤104)
# , the number of test cases.
# For each test case:
# One line containing two integers n
#  and h
#  (1≤n≤105,1≤h≤109)
# , where n
#  represents the number of blankets and h
#  represents the height from the window to the ground.
# Following n
#  lines, each containing two integers w
#  and l
#  (1≤w,l≤109)
# , representing the width and length of each blanket respectively.
# It's guaranteed that the sum of n
#  over all the test cases does not exceed 2×105

# solution

t = int(input())
results = []
for _ in range(t):
    n, h = map(int, input().split())
    total_length = 0
    for _ in range(n):
        w, l = map(int, input().split())
        total_length += max(w, l)
    if total_length >= h:
        results.append("YES")
    else:
        results.append("NO")
print("\n".join(results))