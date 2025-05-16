# BOJ 15652: N과 M (4)
from itertools import combinations_with_replacement
# 디버그 함수 찾기
DEBUG = False
def debug(*args):
    if DEBUG:
        print(*args)

# N, M 입력
N, M = map(int, input().split())

# 조합 생성
base_numbers = [i for i in range(1, N+1)]
result = list(combinations_with_replacement(base_numbers, M))

debug(result)
# 결과 출력
for res in result:
    print(*res)