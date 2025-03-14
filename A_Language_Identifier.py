test_cases = int(input())
for _ in range(test_cases):
    word = input()
    n = len(word)
    if "po" == word[n-2:n]:
        print("FILIPINO")
    elif "mnida" == word[n-5:n]:
        print("KOREAN")
    else:
        print("JAPANESE")