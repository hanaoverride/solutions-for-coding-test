# BOJ 11053: 가장 긴 증가하는 부분수열

# 디버그 함수 및 플래그 정의
DEBUG = False
def debug(*args):
    if DEBUG:
        print(*args)

# N 입력
N = int(input())

# 수열 A 입력
A = list(map(int, input().split()))

# dp[i] = i번째 인덱스의 수로 끝나는 최대 수열 길이로 정의. 기본 길이는 1
dp = [1] * N
# dp 계산 시작: 전수조사
for i in range(N):
    # i번째 수 뒤에 붙을 수 있는 수의 갯수를 조사한다
    for j in range(i):
        # 증가 수열을 만들수 있나요?(단조 증가일 필요가 없다면 등호 포함 가능)
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + 1)
# 최대 길이까지 사용했을때 최적해 출력. 이때 큰 수가 어디인지 알 수 없으므로 max 사용
# (시간을 더 줄이고 싶다면 최대값 계산시 캐싱을 해주면 된다)
print(max(dp))