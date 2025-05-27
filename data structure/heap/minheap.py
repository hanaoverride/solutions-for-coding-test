# BOJ 1927: 최소 힙
import sys
import heapq
input = sys.stdin.readline

# N 입력
N = int(input().strip())

# 최소힙 선언 
min_heap = []

# 결과 배열 선언(가시성 향상)
result = []

# 명령 입력
for _ in range(N):
    command = input().strip()
    # EOF 처리
    if not command:
        break
    node = int(command)
    if node == 0:
        if not min_heap:
            result.append(0)
        else:
            result.append(heapq.heappop(min_heap))
    else:
        heapq.heappush(min_heap, node)
        
# 결과 출력
print(*result, sep='\n')