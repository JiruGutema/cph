from collections import Counter

s = "ADOBECODEBANC"
t = "ABC"
t = Counter(t)

n = len(s)
ans = [0, len(s)-1]
Window = Counter()
left = 0
for right in range(n):
    Window[s[right]] += 1
      
    while Window >= t :
        if (right-left) <= (ans[1] - ans[0]):
            ans[0] = left
            ans[1] = right
        if s[left] in Window:
            Window[s[left]] -= 1
            if Window[s[left]] == 0:
                del Window[s[left]]
        left += 1
print(s[ans[0]:ans[1]+1])