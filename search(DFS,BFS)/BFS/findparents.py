# BOJ 11725: 트리의 부모 찾기
from collections import deque
import bisect
# 디버그 함수 및 플래그 정의
DEBUG = False
def debug(*args):
    if DEBUG:
        print(*args)

# N 입력
N = int(input())

# N개의 트리 연결 입력
# 희소행렬 선언(N=100000 이므로)
sparse = []

for _ in range(N-1):
    k, v = map(int, input().split())
    # 양방향 
    sparse.append((k, v))
    sparse.append((v, k))

# 튜플 원소순으로 오름차순 정렬(최적화를 위해)
sparse.sort()

# 이진 탐색을 위해 unzip(튜플로는 힘들어서)
sparse_s, sparse_e = zip(*sparse)

# 부모 정보 저장
parent = [-1] * (N+1)

# 방문 정보 저장
visited = [False] * (N+1)

# BFS 실행하여 각 노드에 대한 부모-자식 관계 찾기
queue = deque()
queue.append(1)
visited[1] = True
# 희소행렬 탐색 포인터
ptr = 0
debug(sparse_s, len(sparse_s))
debug(sparse_e, len(sparse_e))

while queue:
    curr_node = queue.popleft()
    # 빠른 탐색을 위해 이분검색을 위해 인덱스 탐색.
    ptr = bisect.bisect_left(sparse_s, curr_node)
    debug(f"curr_node, ptr: {curr_node} {ptr}")
    # 현재 노드로 시작하는 희소행렬 원소 탐색
    while ptr < len(sparse_s) and sparse_s[ptr] == curr_node:
        next_node = sparse_e[ptr]
        # 탐색 안했으면 ㄱㄱ
        if not visited[next_node]:
            parent[next_node] = curr_node
            queue.append(next_node)
            visited[next_node] = True
        # 희소행렬의 다음 k, v 탐색
        ptr += 1
# 각 부모 출력
for i in range(2, N+1):
    print(parent[i])