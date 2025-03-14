import sys

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        arr = list(map(int, data[idx:idx+n]))
        idx += n
        out.append(str(sum(arr) - (n - 1)))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
