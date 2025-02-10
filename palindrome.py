def palindrome(num):
    # brute force approach

    numString = str(num)
    print(numString == numString[::-1])
palindrome(121)
