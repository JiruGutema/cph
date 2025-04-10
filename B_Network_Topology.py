from collections import defaultdict

def solve():


    n,m = list(map(int, input().split()))
    adj = defaultdict(list)
    A = []

    for _ in range(m):
        a, b = list(map(int, input().split()))
        A.append([a, b])

    for u, v in A:
        adj[u].append(v)
        adj[v].append(u)

    seen = {}
    nodes = 0
    two = 0
    one = 0

    for u, v in adj.items():
        if len(v) == 2:
            two += 1
        elif len(v) == 1:
            one += 1
        nodes = max(nodes, len(v))
    if two == len(adj):
       return "ring topology"
    
    elif two == len(adj)-2 and one == 2:
        return "bus topology"
    elif one == len(adj) - 1 and nodes == n-1:
        return "star topology"
    else:
        return "unknown topology"
    

print(solve())
