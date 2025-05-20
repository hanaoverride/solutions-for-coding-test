# BOJ 15654: N과 M (5)
from itertools import permutations
# 디버그 함수 및 플래그 정의
DEBUG = False
def debug(*args):
    if DEBUG:
        print(*args)

# N, M 입력
N, M = map(int, input().split())

# 수 배열 입력
numbers = list(map(int, input().split()))

# 증가순 유지를 위해 정렬
numbers.sort()

# 순열 출력
for p in permutations(numbers, M):
    print(*p)