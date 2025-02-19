test_cases = int(input())

for _ in range(test_cases):
    s = input()
    def is_palindrome(s):
        return s == s[::-1]

    def min_erased(s, left, right):
        if left >= right:
            return 0
        if s[left] == s[right]:
            return min_erased(s, left + 1, right - 1)
        else:
            return 1 + min(min_erased(s, left + 1, right), min_erased(s, left, right - 1))


    min_erased_count = min_erased(s, 0, len(s) - 1)
    print(min_erased_count if min_erased_count <= len(s) else -1)

