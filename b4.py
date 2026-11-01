import sys


def next_combination(a, n, k):
  i = k - 1
  while i >= 0 and a[i] == n - k + i + 1:
    i -= 1
  if i < 0:
    return None
  a[i] += 1
  for j in range(i + 1, k):
    a[j] = a[j - 1] + 1
  return a


def solve():
  input_data = sys.stdin.read().split()
  if not input_data:
    return
  n = int(input_data[0])
  k = int(input_data[1])
  t = int(input_data[2])

  a = [int(x) for x in input_data[3 : 3 + k]]

  count = 0
  current_a = list(a)
  while count < t:
    res = next_combination(current_a, n, k)
    if res is None:
      break
    print(*(current_a))
    count += 1

  if count < t:
    print(0)


if __name__ == "__main__":
  solve()