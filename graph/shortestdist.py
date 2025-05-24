# BOJ 1916: 최소비용
# 디버그 함수 및 플래그 정의
import sys
import heapq
input = sys.stdin.readline
DEBUG = False
def debug(*args):
    if DEBUG:
        print(*args)

# N, M 입력
N, M = int(input().strip()), int(input().strip())

# 인접행렬 선언
# TODO: N이 커지면 희소행렬이나 인접리스트 기반 구현이 좋음
adj = [[99999999]*(N+1) for _ in range(N+1)]

# 자기 자신에 대한 비용 계산
for i in range(1, N+1):
    adj[i][i] = 0
    
# 간선 정보 입력
for _ in range(M):
    start, end, weight = map(int, input().split())
    adj[start][end] = min(adj[start][end], weight)

# 비용 배열 정의: cost[n] = 시작점부터 n 노드까지의 최소비용
cost = [99999999] * (N+1)

# 시작, 끝 노드 정의
start, end = map(int, input().split())
# 시작점 비용은 0
cost[start] = 0
priority_queue = [(0, start)]

# 다익스트라 실행
while priority_queue:
    distance, curr_node = heapq.heappop(priority_queue)
    debug("cost: ")
    debug(cost)
    for i in range(1, N+1):
        if adj[curr_node][i] != 99999999 and distance + adj[curr_node][i] < cost[i]:
            cost[i] = distance + adj[curr_node][i]
            heapq.heappush(priority_queue, (cost[i], i))

# 결과값 출력
print(cost[end])