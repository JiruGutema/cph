n = int(input())

for i in range(n):
    t1, t2 = map(str, input().split(" "))

    if t1[-1] != t2[-1]:
        if t1[-1] == "M" and t2[-1] == "L":
            print("<")
        elif t1[-1] == "L" and t2[-1] == "M":
            print(">")
        
        elif t1[-1] == "S" and t2[-1] == "M":
            print("<")
        
        elif t1[-1] == "M" and t2[-1] == "S":
            print(">")
        
        elif t1[-1] == "L" and t2[-1] == "S":
            print(">")
        elif t1[-1] == "S" and t2[-1] == "L":
            print("<")
        
    else:
        if len(t1) > len(t2) and t2[-1] == "S":
            print("<")
        elif len(t1) < len(t2) and t2[-1] == "S":
            print(">")
        elif len(t1) < len(t2):
            print("<")
        elif len(t1) == len(t2):
            print("=")
        else:
            print(">")
