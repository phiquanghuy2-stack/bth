import sys


def solve():
  line = sys.stdin.read().split()
  if not line:
    return
  N = int(line[0])
  l = int(line[1])
  u = int(line[2])

  ans = 0
  start = max(0, l)
  end = min(N, u)
  for x0 in range(start, end + 1):
    S = N - x0
    ans += S + 1  # Số nghiệm của x1 + x2 = S là S + 1
  print(ans)


if __name__ == "__main__":
  solve()