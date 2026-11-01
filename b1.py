import sys


def solve():
  input_data = sys.stdin.read().split()
  if not input_data:
    return
  n = int(input_data[0])
  A = [int(x) for x in input_data[1 : n + 1]]
  B = [int(x) for x in input_data[n + 1 : 2 * n + 1]]

  intersection = []
  for i in range(n):
    if A[i] == 1 and B[i] == 1:
      intersection.append(i + 1)  # Chỉ số i biểu thị phần tử i+1

  q = len(intersection)
  print(q)
  if q > 0:
    print(*(intersection))


if __name__ == "__main__":
  solve()