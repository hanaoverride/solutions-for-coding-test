# BOJ 1010: 다리 놓기
# 함수의 injectiveness의 비유같음??
# 아... 근데 겹쳐질수 없어서 좀 다를거같음
# 규칙성 찾아보기 (1,1) = 1, (1,2) = 2, ...
# (2,2) = 1, (2,3) = 3, (2,4) = 6, ...
# (3,3) = 1, (3,4) = 4, (3,5) = 30, ...
# dp[N][M] = C(M,N)??
from math import comb

DEBUG = False
# 디버깅용 함수 정의
def debug(*args):
    if DEBUG:
        print(*args)

# 테스트 케이스 입력
T = int(input())

# 입력 iteration
for _ in range(T):
    N, M = map(int, input().split())
    print(comb(M,N))