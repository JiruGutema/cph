test_cases = int(input())

for _ in range(test_cases):
    n,m = list(map(int, input().split()))
    a2svians = list(map(int, input().split()))

    a2svians.sort()
    length = len(a2svians)

    middle = length//2 -1
    end = length-1

    diff = m
    flag = "YES"
    while middle >= 0:
        
        if a2svians[end] - a2svians[middle] < diff:
            flag = ("NO")
            break
        middle -= 1
        end -= 1
    print(flag)

