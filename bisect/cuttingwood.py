# BOJ 2805: 나무 자르기
import sys
import bisect
from math import ceil
input = sys.stdin.readline

# 디버그 함수 및 플래그 정의
DEBUG = False
def debug(*args):
    if DEBUG:
        print(*args)
        
# N, M 입력
N, M = map(int, input().split())

# 나무 길이 입력
tree = list(map(int, input().split()))

# 절단 용이를 위해 정렬 ~ N log N
# ex. 20 17 15 10이라면...
# 20 - 0
# 17 - 3 - 3이 1개
# 15 - 2 2+(3) - 2가 2개
# 10 - 5 5+(2) 5+(2+3) 5가 3개
tree.sort(reverse=True)

# 규칙성을 찾았으니 절단량을 비교할 배열을 새로 만들자(역순)
cutter = []
for i in range(N-1):
    # 위에 명시한 규칙을 식으로 옮겼습니다
    passage = (tree[i] - tree[i+1])*(i+1) + (cutter[-1] if cutter else 0)
    cutter.append(passage)

# 이분검색을 통해 조건을 만족하는 최소 ptr 탐색 ~ log N
ptr = bisect.bisect_left(cutter, M)
debug(f"tree: {tree}")
debug(f"cutter: {cutter}")
debug(f"ptr: {ptr}")

# 공통 공식 적용
start = cutter[ptr-1] if ptr > 0 else 0
# 절단 길이는 항상 ptr + 1
# cutter 배열은 인접 원소의 차로 정의되므로 항상 갯수와 인덱스가 1만큼 작다.
# 따라서 길이는 +1을 해줘야 맞음
mul = ptr + 1
# 가장 가까운 절단길이를 찾음.
count = ceil((M - start) / mul)

# 이분검색 결과에서 가장 가까운 절단길이만큼 더 자르면 그게 결과!
print(tree[ptr] - count)
