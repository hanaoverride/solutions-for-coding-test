# BOJ 2839: 설탕 배달

# 디버그 함수 및 플래그 정의
DEBUG = False
def debug(*args):
    if DEBUG:
        print(*args)
        
# N 입력
N = int(input())

# dp 배열 정의 (N <= 5000)
# dp[weight] = weight만큼의 무게를 사용 가능할때 최소 주머니 갯수
default_max = 100000000
dp = [default_max] * 5001

# 3과 5를 만드는 가장 작은 방법 미리 설정
dp[3] = 1
dp[5] = 1

debug("N: " + str(N))
# dp 시작
for weight in range(6, N + 1):
    debug(f"dp[weight]: {dp[weight]} ")
    debug(f"dp[weight-3]: {dp[weight-3]} ")
    debug(f"dp[weight-5]: {dp[weight-5]} ")
    # 3짜리를 더할까? 5짜리를 더할까?
    dp[weight] = min(dp[weight], dp[weight-3] + 1)
    dp[weight] = min(dp[weight], dp[weight-5] + 1)
    
debug(dp)
# 결과 출력
result = -1 if dp[N] == default_max else dp[N]
print(result)
    