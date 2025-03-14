import sys, math
from functools import cmp_to_key
from operator import itemgetter
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque

input = sys.stdin.readline

def iinp(): return (int(input()))
def linp(): return (list(map(int, input().split())))
def sinp(): return (input().strip())
def minp(): return (map(int, input().split()))
def solve():
    # Read number of test cases
    t = int(input())
    
    # Process each test case
    for _ in range(t):
        # Read the value of n (size of the permutation)
        n = int(input())
        # Read the permutation array
        p = list(map(int, input().split()))
        
        # Count how many descending pairs there are
        odd_subarrays = 0
        for i in range(n - 1):
            if p[i] > p[i + 1]:
                odd_subarrays += 1
        
        # The maximum number of odd subarrays is one more than the number of descending pairs
        # as there will be a single odd subarray at the end
        print(odd_subarrays + 1)

# Call the solve function to execute the solution
solve()



def main():
    solve()


if __name__ == "__main__":
    main()