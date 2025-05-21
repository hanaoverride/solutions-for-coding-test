# BOJ 1149: RGB거리
# 디버그 함수 및 플래그 정의
DEBUG = False
def debug(*args):
    if DEBUG:
        print(*args)
        
# N 입력
N = int(input())

# 비용 입력 
cost = [list(map(int, input().split())) for _ in range(N)]

# dp 배열 정의 dp[i][color] = i번째 집의 color일때 최소 비용
dp = [[0] * 3 for i in range(N)]
dp[0][0], dp[0][1], dp[0][2] = cost[0][0], cost[0][1], cost[0][2]

# dp 전략: 현재 색이 color면 이전 값에서 color 이외를 골랐어야 함.
for i in range(1, N):
    for j in range(3):
        mini = 99999999
        for k in range(3):
            if j != k:
                mini = min(mini, dp[i-1][k] + cost[i][j])
        dp[i][j] = mini
    debug(dp)
# dp 결과 출력
print(min(dp[N-1]))