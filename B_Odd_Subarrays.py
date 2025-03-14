import sys

input = sys.stdin.readline

def iinp(): return (int(input()))
def linp(): return (list(map(int, input().split())))
def sinp(): return (input().strip())
def minp(): return (map(int, input().split()))

def solve():
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        p = list(map(int, input().split()))
        
        odd_subarrays = 0
        for i in range(n - 1):
            if p[i] > p[i + 1]:
                odd_subarrays += 1
        
        print(odd_subarrays + 1)



def main():
    solve()

if __name__ == "__main__":
    main()