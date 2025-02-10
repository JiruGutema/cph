n = int(input())
s = input()
if n in [0, 1]:
    print(s)
else:
    newString = ""
    i = 0
    addon = 2
    while i < n:
        newString += s[i]
        i += addon
        addon += 1
    print(newString)