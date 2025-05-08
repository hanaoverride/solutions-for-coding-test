# BOJ 1003: 피보나치 함수
DEBUG = False
# 디버깅용 함수 정의
def debug(*args):
    if DEBUG:
        print(*args)

# 테스트 케이스 입력
T = int(input())
count_zero = [0] * 41
count_one = [0] * 41

count_zero[0] = 1
count_one[1] = 1

# preprocessing
for i in range(2, 41):
    count_zero[i] = count_zero[i-1] + count_zero[i-2]
    count_one[i] = count_one[i-1] + count_one[i-2]
    
# 각 경우에 대해 iterate
for _ in range(T):
    N = int(input())
    print(str(count_zero[N]) + " " +  str(count_one[N]))
    
