# 프로그래머스 레벨 2: 게임 맵 최단거리
from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    # 탐색한 배열 체크
    visited = [[False for col in range(m)] for row in range(n)]
    # 방향 배열 생성
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    # 정답치 선언: 초기 값은 큰 값을 집어넣는다
    answer = 100000000
    # 큐 선언
    q = deque()

    # 큐에 초기 탐색값 삽입:
    # (x, y, count)
    q.append((0,0,1))
    visited[0][0] = True
    
    # 최단거리 체크를 위해 BFS 실행
    while q:
        # x, y 좌표 및 count 추출
        cur_x, cur_y, count = q.popleft()
        
        # 목적지 도착시
        if cur_x == n - 1 and cur_y == m - 1:
            return count
            
        # 4가지 방향에 대해 탐색
        for direction in directions:
            # direction tuple에서 증분 추출
            inc_x, inc_y = direction
            new_x, new_y = cur_x + inc_x, cur_y + inc_y
            
            # 좌표가 맵 안에 있고 지나갈 수 있는 길인가?
            if 0 <= new_x < n and 0 <= new_y < m:
                if maps[new_x][new_y] == 1 and not visited[new_x][new_y]:
                    # 현재 위치 방문 체크
                    visited[new_x][new_y] = True
                    # 새로 탐색할 노드
                    q.append((new_x, new_y, count + 1))
                    
    # 초기값 유지시 탐색 실패로 간주                
    return -1