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

def max_prefix_sum(arr):
    max_sum, curr_sum = 0, 0
    for num in arr:
        curr_sum += num
        max_sum = max(max_sum, curr_sum)
    return max_sum

def solve():
    t = int(input())  
    results = []
    
    for _ in range(t):
        n = int(input())  
        r = list(map(int, input().split()))  
        m = int(input())  
        b = list(map(int, input().split()))  

        
        max_r = max_prefix_sum(r)
        max_b = max_prefix_sum(b)
        
        
        results.append(str(max_r + max_b))

    print("\n".join(results))  



def main():
    test_cases = 1
    
    for _ in range(test_cases):
        solve()

if __name__ == "__main__":
    main()