n = int(input())
for i in range(n):
    s = input()
    t = input()
    p = input()
    
    s += p
    s = sorted(s)
    s = "".join(s)
    t = "".join(sorted(t))

    if t in s:
        print("YES")
    else:
        print("NO")

