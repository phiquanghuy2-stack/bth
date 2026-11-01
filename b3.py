import sys


def solve():
  input_data = sys.stdin.read().split()
  if not input_data:
    return
  n = int(input_data[0])

  E = 1  # Số xâu độ dài 0 có chẵn chữ số 0 (xâu rỗng)
  O = 0  # Số xâu độ dài 0 có lẻ chữ số 0

  for i in range(1, n + 1):
    next_E = 9 * E + O
    next_O = 9 * O + E
    E, O = next_E, next_O

  print(E)


if __name__ == "__main__":
  solve()