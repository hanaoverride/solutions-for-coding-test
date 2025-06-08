# BOJ 1389: 케빈 베이컨의 6단계 법칙
import sys
input = sys.stdin.readline

DEBUG = False
def debug(*args):
    if DEBUG:
        print(*args)
        
N, M = map(int, input().split())

graph = [[10**10]*(N+1) for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    graph[s][e] = 1
    graph[e][s] = 1
    
# 각 노드에 대해 플로이드-워셜
for middle in range(1, N+1):
    for start in range(1, N+1):
        for end in range(1, N+1):
            # 경유해서 가는게 빠른가?
            graph[start][end] = min(graph[start][end], graph[start][middle] + graph[middle][end])

debug(*graph[1:])

min_connection = (10**10, None)

# 최소값 탐색
for member in range(1, N+1):
    line_sum = sum(graph[member][1:])
    if min_connection[0] > line_sum:
        min_connection = (line_sum, member)
        
print(min_connection[1])