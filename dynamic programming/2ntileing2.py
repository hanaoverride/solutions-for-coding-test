# BOJ 11727: 2*n 타일링 2
import sys
input = sys.stdin.readline

DEBUG = False
def debug(*args):
    if DEBUG:
        print(*args)
        
n = int(input().strip())

dp = [0] * 1001

dp[1] = 1
dp[2] = 3

for size in range(3, n+1):
    # 2:1-> size-1
    # 1:2-> size-2
    # 2:2-> size-2
    dp[size] = (dp[size-1] + 2*dp[size-2]) % 10007

print(dp[n])