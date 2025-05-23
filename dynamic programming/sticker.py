# BOJ 9465: 스티커
# 디버그 함수 및 플래그 정의
import sys
input = sys.stdin.readline
DEBUG = False
def debug(*args):
    if DEBUG:
        print(*args)

# 테스트 케이스 T 입력
T = int(input().strip())

# 문제해결 함수 solve 정의
def solve():
    # n 입력
    n = int(input().strip())
    
    # 스티커 배열 정의
    sticker = [[0]*n for _ in range(2)]
    
    # 윗쪽 스티커 맵 입력
    sticker[0] = list(map(int, input().split()))
    # 아래쪽 스티커 맵 입력
    sticker[1] = list(map(int, input().split()))
    
    # dp 배열 정의
    # 스티커가 인접하지 않게 완성하는 방법은 두칸 이전에서 붙이거나,
    # 한칸 이전의 반대쪽에서 붙이는 방법이 있다. 
    dp = [[0]*n for _ in range(2)]
    
    # 초기 조건 삽입
    # case 1: i = 0
    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]
    
    # case 2: i=1
    if n >= 2:
        dp[0][1] = dp[1][0] + sticker[0][1]
        dp[1][1] = dp[0][0] + sticker[1][1]
    
    # dp 계산 시작
    for i in range(2, n):
        for j in range(2):
            maxi = -1
            for k in range(2):
                # case 1: 2칸 이전에서 왔음?
                # 현재 스티커: sticker[j][i]
                # 2칸 이전 스티커(case 2개): dp[k][i-2]
                maxi = max(maxi, dp[k][i-2] + sticker[j][i])
                if j != k:
                    # 1칸 이전 스티커: dp[k][i-1]
                    maxi = max(maxi, dp[k][i-1] + sticker[j][i])
            dp[j][i] = maxi
    
    # dp 결과 출력
    print(max(dp[0][n-1], dp[1][n-1]))
                
# 테스트케이스 횟수만큼 solve
for _ in range(T):
    solve()