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

def precompute_prefix_sums(arr):
    prefix = [0] * (len(arr) + 1)
    for i in range(1, len(arr) + 1):
        prefix[i] = prefix[i - 1] + arr[i - 1]
    return prefix

def solve():
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    n = int(data[index])
    index += 1
    
    v = list(map(int, data[index:index + n]))
    index += n
    
    prefix_original = precompute_prefix_sums(v)
    
    sorted_v = sorted(v)
    prefix_sorted = precompute_prefix_sums(sorted_v)
    
    m = int(data[index])
    index += 1
    
    result = []
    
    for _ in range(m):
        query_type, l, r = map(int, data[index:index + 3])
        index += 3
        
        if query_type == 1:
            result.append(str(prefix_original[r] - prefix_original[l - 1]))
        else:
            result.append(str(prefix_sorted[r] - prefix_sorted[l - 1]))

    sys.stdout.write("\n".join(result) + "\n")



def main():
    test_cases = 1
    for _ in range(test_cases):
        solve()

if __name__ == "__main__":
    main()