import sys


def solve():
  input_data = sys.stdin.read().split()
  if not input_data:
    return
  n = int(input_data[0])
  r = int(input_data[1])

  fixed = {}
  idx = 2
  for _ in range(r):
    u = int(input_data[idx])
    v = int(input_data[idx + 1])
    fixed[u] = v
    idx += 2

  results = []
  used = [False] * (n + 1)
  current = [0] * n

  valid_init = True
  assigned_vals = set()
  for u, v in fixed.items():
    if v in assigned_vals:
      valid_init = False
      break
    assigned_vals.add(v)
    used[v] = True
    current[u] = v

  def backtrack(pos):
    if pos == n:
      results.append(list(current))
      return
    if pos in fixed:
      backtrack(pos + 1)
      return

    for val in range(1, n + 1):
      if not used[val]:
        used[val] = True
        current[pos] = val
        backtrack(pos + 1)
        used[val] = False
        current[pos] = 0

  if valid_init:
    backtrack(0)

  if not results:
    print(0)
  else:
    for p in results:
      print(*(p))


if __name__ == "__main__":
  solve()