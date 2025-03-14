import sys

def count_integer_points(n, m, x, r):
    points = set()
    
    for i in range(n):
        xi = x[i]
        ri = r[i]
        

        for x_val in range(xi - ri, xi + ri + 1):
    
            y_max = int((ri**2 - (x_val - xi)**2)**0.5)
            
    
            for y_val in range(-y_max, y_max + 1):
                points.add((x_val, y_val))
    
    return len(points)

def main():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(t):
        n = int(data[idx])
        m = int(data[idx + 1])
        idx += 2
        
        x = list(map(int, data[idx:idx + n]))
        idx += n
        
        r = list(map(int, data[idx:idx + n]))
        idx += n
        
        result = count_integer_points(n, m, x, r)
        results.append(result)
    
    sys.stdout.write("\n".join(map(str, results)) + "\n")

if __name__ == "__main__":
    main()