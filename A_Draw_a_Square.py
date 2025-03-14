def is_square(l, r, d, u):
    p1 = (-l, 0)
    p2 = (r, 0)
    p3 = (0, -d)
    p4 = (0, u)
    
    def sqdist(p, q):
        return (p[0] - q[0])**2 + (p[1] - q[1])**2
    
    pts = [p1, p2, p3, p4]
    dists = []
    for i in range(4):
        for j in range(i+1, 4):
            dists.append(sqdist(pts[i], pts[j]))
    dists.sort()
    
    if dists[0] == 0:
        return False
    if dists[0] == dists[1] == dists[2] == dists[3] and dists[4] == dists[5] and dists[4] == 2 * dists[0]:
        return True
    return False

t = int(input())
for _ in range(t):
    l, r, d, u = map(int, input().split())
    print("Yes" if is_square(l, r, d, u) else "No")
