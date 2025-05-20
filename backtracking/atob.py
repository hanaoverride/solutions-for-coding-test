# BOJ 16953: A -> B
from collections import deque
# 디버그 함수 및 플래그 정의
DEBUG = False
def debug(*args):
    if DEBUG:
        print(*args)

# 정방향으로 수를 완성하는것보다 역방향으로 수를 만드는게 더 쉽다.
# 다행히 연산이 결정론적이기 때문에 두 연산에 대해 역연산을 완벽하게 정의할 수 있다.
# *2 -> /2(2의 배수인 경우만), 1 추가 -> 1 떼기(끝자리가 1인 경우만)

# A, B 입력
A, B = map(int, input().split())

# 스택 선언(초기값은 B)
stack = deque()
stack.append((B, 1))

# 결과값 저장
result = 99999999

# 탐색 시작: DFS(나중에 안건데 최단경로라 BFS가 더 빠르다고함)
while stack:
    # 값 추출
    curr_num, curr_count = stack.pop()
    # 목표치 도달
    if curr_num == A:
        result = min(result, curr_count)
        continue
    # 두 역연산이 모두 작아지는 연산이므로 이미 A보다 작아졌다면 더 탐색하는게 의미가 없다.
    elif curr_num < A:
        continue
    # 두개의 경우에 대해 탐색
    if curr_num % 2 == 0:
        stack.append((curr_num // 2, curr_count + 1))
    if curr_num % 10 == 1:
        stack.append((curr_num // 10, curr_count + 1))

print(-1 if result == 99999999 else result)