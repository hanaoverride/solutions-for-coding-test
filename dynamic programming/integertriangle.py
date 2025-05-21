# BOJ 1932: 정수 삼각형
# 디버그 함수 및 플래그 정의
DEBUG = False
def debug(*args):
    if DEBUG:
        print(*args)
        
# N 입력
N = int(input())

# 수 삼각형 입력
triangle = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]

debug(triangle)

dp[0][0] = triangle[0][0]

# dp 계산 시작:
for i in range(1, N):
    for j in range(i+1):
        maxi = -1
        # 왼쪽
        if j-1 >= 0:
            maxi = max(maxi, dp[i-1][j-1] + triangle[i][j])
        # 오른쪽
        if j < i:
            maxi = max(maxi, dp[i-1][j] + triangle[i][j])
        dp[i][j] = maxi
    debug(dp)

# 최대 경로합 출력
print(max(dp[N-1]))