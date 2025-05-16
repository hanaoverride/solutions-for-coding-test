# BOJ 2798: 블랙잭
# 디버그 함수 및 플래그 정의
DEBUG = False
def debug(*args):
    if DEBUG:
        print(*args)
        
# N, M 입력받기
N, M = map(int, input().split())

# 카드풀 배열 선언
card_pool = list(map(int, input().split()))
result = -1

debug(f"(N,M) = {(N, M)}")
debug(card_pool)

# 3장의 합이 고정되어있고 순서가 고정되어있으므로 3중 for문 사용
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            combination = card_pool[i] + card_pool[j] + card_pool[k]
            if combination <= M:
                result = combination if combination > result else result

# 결과 출력
print(result)