test_cases = int(input())
for _ in range(test_cases):
    kicks = list(input().strip())

    score1 = [0 , 0]
    score2 = [0 , 0]
    remain1 = 5
    remain2 = 5
    for i in range(10):
        if i%2 == 0:
            if kicks[i] == "1":
                score1[0] += 1
                score1[1] += 1
            elif kicks[i] == "?":
                score1[1] += 1
            remain1 -= 1
        else:
            if kicks[i] == "1":
                score2[0] += 1
                score2[1] += 1
            elif kicks[i] == "?":
                score2[1] += 1
            remain2 -= 1
        case_1 = score1[1] - score2[0]
        case_2 = score2[1] - score1[0]

        if (case_1 > remain2) or (case_2 > remain1):
            print(i+1)
            break
        if remain1 == remain2 == 0:
            print(10)
            
        
        
    