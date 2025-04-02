test_cases = int(input())

for _ in range(test_cases):
    neighbor = (input())
    n = len(neighbor)

    curr = neighbor[0]
    prev = (int(curr)-1)*10
    if n == 1:
        print(prev + 1) 
    elif n == 2:
        print(prev + 3)
    elif n == 3:
        print(prev + 6)
    else:
        print(prev + 10)

