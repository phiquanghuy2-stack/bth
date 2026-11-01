import sys


def solve():
  input_data = sys.stdin.read().split()
  if not input_data:
    return
  n = int(input_data[0])
  k = int(input_data[1])

  current = []
  used = [False] * (n + 1)

  def backtrack():
    if len(current) == k:
      print(*(current))
      return

    for i in range(1, n + 1):
      if not used[i]:
        used[i] = True
        current.append(i)
        backtrack()
        current.pop()
        used[i] = False

  backtrack()


if __name__ == "__main__":
  solve()