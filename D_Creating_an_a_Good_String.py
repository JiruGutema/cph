test_cases = int(input())

for _ in range(test_cases):
    first_half = 0
    second_half = 0
    n= int(input())
    i = 0
    j = n//2
    string = list((input()))
    idx = 0 
    if n != 1:
        while idx < n//2:
        
            if string[i+idx] != "a":
                first_half += 1
            if string[j+idx] != "a":
                second_half += 1
            idx += 1
        print(min(first_half, second_half))
    else:
        print(0) if string[0] == "a" else print(1)
        

