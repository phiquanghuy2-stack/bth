import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    k = int(data[1])

    # dp[j]: số xâu hợp lệ hiện tại kết thúc bằng đúng j số 0 liên tiếp
    dp = [0] * k
    dp[0] = 1

    for _ in range(n):
        new_dp = [0] * k
        # Thêm '1' vào cuối -> số lượng số 0 liên tiếp ở cuối về 0
        new_dp[0] = sum(dp)
        # Thêm '0' vào cuối -> tăng số lượng số 0 liên tiếp lên 1
        for j in range(1, k):
            new_dp[j] = dp[j - 1]
        dp = new_dp

    print(sum(dp))

if __name__ == '__main__':
    solve()