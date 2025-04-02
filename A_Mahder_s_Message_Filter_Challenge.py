test_cases = int(input())

for _ in range(test_cases):
    n = int(input())
    msg = input()

    end = 0
    j = n-1
    while j >= 0 and msg[j] == ")":
        end += 1
        j -= 1
        
    if end > n // 2:
        print("Yes")
    else:
        print("No")


    