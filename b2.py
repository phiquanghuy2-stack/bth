import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    k = int(data[1])

    fixed = [0] * (n + 1)  
    used = [False] * (n + 1)

    idx = 2
    for _ in range(k):
        u = int(data[idx])
        v = int(data[idx + 1])
        idx += 2

        if fixed[u] != 0:
            if fixed[u] != v:
                print(0)
                return
            continue
        if used[v]:
            print(0)
            return

        fixed[u] = v
        used[v] = True

    perm = [0] * (n + 1)
    out = []

    def backtrack(pos):
        if pos > n:
            out.append(" ".join(map(str, perm[1:])))
            return

        if fixed[pos] != 0:
            perm[pos] = fixed[pos]
            backtrack(pos + 1)
        else:
            for val in range(1, n + 1):
                if not used[val]:
                    used[val] = True
                    perm[pos] = val
                    backtrack(pos + 1)
                    used[val] = False

    backtrack(1)

    if not out:
        print(0)
    else:
        sys.stdout.write("\n".join(out) + "\n")

if __name__ == '__main__':
    solve()