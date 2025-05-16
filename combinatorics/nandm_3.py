# BOJ 15651: N과 M (3)
from itertools import product
# 디버그 함수 찾기
DEBUG = False
def debug(*args):
    if DEBUG:
        print(*args)

# N, M 입력
N, M = map(int, input().split())

# 조합 생성
base_numbers = [i for i in range(1, N+1)]
result = list(product(base_numbers, repeat=M))

debug(result)
# 결과 출력
for res in result:
    print(*res)