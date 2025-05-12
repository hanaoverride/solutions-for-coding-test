# BOJ 11047: 동전 0

# 디버그 함수 및 플래그 정의
DEBUG = False
def debug(*args):
    if DEBUG:
        print(*args)
        
# N, K 입력
N, K = map(int, input().split())

# 동전의 가치를 저장하는 coin 배열 정의
coin = [0] * N

# 갯수를 셀 수 있는 count 변수 정의
count = 0

# 동전을 입력
for i in range(N):
    coin[i] = int(input())

# 각 동전의 가치가 배수 관계가 성립하므로 p진수 표현처럼 최소 갯수가 될 수 있는 동전 분배 방식이 항상 유일함.
# 가장 큰 가치부터 절사하여 분배하자
for index in range(N-1, -1, -1):
    value = coin[index]
    debug("value: " + str(value))
    
    # 동전 분배 
    count += K // value
    debug("count: " + str(count))
    
    # 거스름돈
    K %= value
    debug("K: " + str(K))

print(count)