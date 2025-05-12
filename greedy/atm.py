# BOJ 11399: ATM

# 디버그 함수 및 플래그 정의
DEBUG = False
def debug(*args):
    if DEBUG:
        print(*args)
        
# N 입력
N = int(input())

# time을 저장하는 배열 정의
time = [0] * N

# 입력 횟수만큼 iteration
input_array = input().split()
for i in range(N):
    time[i] = int(input_array[i])

# 유일 최적해는 가장 작은 시간 걸리는 경우부터 무조건 처리해주는 방식이다.
# 해를 내는 방법이 유일하여 그리디를 사용할 수 있다.
# 이는 문제에서 제시하는 test case를 살펴보면 규칙이 보인다.
# CPU 스케쥴링 방식 중 하나가 생각나네요!
time.sort()

# 한편 총 걸리는 시간은 내가 처리하는 시간 외에 뒤에 기다리고 있는 사람들이 배로 겪어준다.
# 따라서, i번째로 처리받는 사람은 N-i배의 처리시간을 받는다(0<=i<N, 1<=multiplier<=N)
result = 0
for i in range(N):
    result += (N-i)*time[i]
    
# 결과값 출력
print(result)