# BOJ 1753: 최단경로
# 디버그 함수 및 플래그 정의
import sys
import heapq
input = sys.stdin.readline
DEBUG = False
def debug(*args):
    if DEBUG:
        print(*args)

# V, E 입력
V, E = map(int, input().split())

# 시작 정점 K 입력
K = int(input().strip())

# 정점 V가 가진 인접 정점 리스트를 멤버로 갖는 인접 리스트 정의
adj = [[] for _ in range(V+1)]

# 간선 입력
for _ in range(E):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))

# K부터 x까지 비용: cost[x] 정의
cost = [10**10] * (V+1)
cost[K] = 0

# 다익스트라 시작
priority_queue = [(0, K)]

while priority_queue:
    distance, curr_node = heapq.heappop(priority_queue)
    
    # 간선 탐색 ~ adj(v)
    for v, w in adj[curr_node]:
        if distance + w < cost[v]:
            cost[v] = distance + w
            heapq.heappush(priority_queue, (distance + w, v))
            
# 각 비용 출력
for i in range(1, V+1):
    print(cost[i] if cost[i] != 10**10 else 'INF')