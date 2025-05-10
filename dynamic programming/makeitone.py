# BOJ 1463: 1로 만들기

# 디버그 함수 및 플래그 정의
DEBUG = False
def debug(*args):
    if DEBUG:
        print(*args)
        
# N 입력
N = int(input())

# dp 배열 정의 (N <= 1000000)
# dp[number] = number만큼의 수가 있을때 1을 만드는 최소 연산 횟수
default_max = 100000000
dp = [default_max] * 1000001

# 연산을 사용하는 가장 작은 횟수 미리 설정
dp[1] = 0 # 연산을 안해도 이미 1임
dp[2] = 1 # 2번 연산 혹은 3번 연산 1회.
dp[3] = 1 # 1번 연산 1회.

debug("N: " + str(N))

# dp 시작
for number in range(4, N + 1):
    if number % 3 == 0:
        dp[number] = min(dp[number], dp[number // 3] + 1)
    if number % 2 == 0:
        dp[number] = min(dp[number], dp[number // 2] + 1)
    dp[number] = min(dp[number], dp[number - 1] + 1)
    
# 결과 출력
print(dp[N])