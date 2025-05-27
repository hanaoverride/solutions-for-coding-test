# BOJ 11286: 절댓값 힙
import sys
import heapq
input = sys.stdin.readline

# N 입력
N = int(input().strip())

# 절댓값 힙 선언 
abs_heap = []

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
        if not abs_heap:
            result.append(0)
        else:
            abs_val, val = heapq.heappop(abs_heap)
            result.append(val)
    else:
        heapq.heappush(abs_heap, (abs(node), node))
        
# 결과 출력
print(*result, sep='\n')