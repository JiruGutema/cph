n = int(input())
for i in range(n):
    s = input()
    if len(s) > 1 and s[len(s)//2:] == s[:len(s)//2]:
        print("YES")
    else:
        print("NO")