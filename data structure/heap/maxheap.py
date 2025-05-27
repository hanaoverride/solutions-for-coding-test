# BOJ 11279: 최대 힙
import sys
import heapq
input = sys.stdin.readline

# N 입력
N = int(input().strip())

# 최대힙 선언 
max_heap = []

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
        if not max_heap:
            result.append(0)
        else:
            result.append(-heapq.heappop(max_heap))
    else:
        heapq.heappush(max_heap, -node)
        
# 결과 출력
print(*result, sep='\n')