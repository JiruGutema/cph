from collections import deque

n,k = list(map(int, input().split()))
ids = list(map(int, input().split()))

curr_display = deque()
display_set = set()

for id in ids:
    if id in display_set:
        continue
    if len(curr_display) == k:
        removed_id = curr_display.pop()
        display_set.remove(removed_id)
    curr_display.appendleft(id)
    display_set.add(id)
    
print(len(curr_display))
print(*(curr_display))