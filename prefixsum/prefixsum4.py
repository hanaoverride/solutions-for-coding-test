# BOJ 11659번: 구간 합 구하기 4

# 디버그 함수 생성
DEBUG = False
def debug(*args):
    if DEBUG:
        print(*args)
        
# N, M 입력
N, M = map(int, input().split())

# N개의 입력값 입력
numbers = list(map(int,input().split()))
debug(numbers)
# dp 배열 생성 (dp[i] = i번째 값까지의 연속합)
dp = [0] * N
dp[0] = numbers[0]
# dp 계산
for i in range(1, N):
    dp[i] = dp[i-1] + numbers[i]

# M개의 구간 입력
for _ in range(M):
    i, j = map(int, input().split())
    # 0-based index에 맞춰 보정
    i, j = i-1, j-1
    
    # 구간 합 계산 후 출력(중복 차감은 보정)
    print(dp[j] - dp[i] + numbers[i])
    