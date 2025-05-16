# BOJ 2606번: 바이러스
from collections import deque
# 디버그 함수 찾기
DEBUG = False
def debug(*args):
    if DEBUG:
        print(*args)

# 컴퓨터의 수 입력
number_of_computers = int(input())

# 연결 선의 갯수
number_of_links = int(input())

# 인접행렬 정의
adj = [[False] * (number_of_computers + 1) for _ in range(number_of_computers + 1)]

# 방문 노드 배열 정의
visited = [False] * (number_of_computers + 1)

# 연결 선 입력(양방향)
for _ in range(number_of_links):
    start, end = map(int, input().split())
    adj[start][end] = adj[end][start] = True

# DFS 실행(BFS도 무방할거같은데 걍 이걸로 해봄)
stack = deque()
# 1번 컴퓨터부터 탐색 시작
stack.append(1)
# 결과값 변수 정의
result = 0
while stack:
    current_computer = stack.pop()
    if visited[current_computer]:
        continue
    visited[current_computer] = True
    result += 1
    for i in range(1, number_of_computers + 1):
        if not visited[i] and adj[current_computer][i]:
            stack.append(i)

# 1번 컴퓨터는 제외
print(result - 1)