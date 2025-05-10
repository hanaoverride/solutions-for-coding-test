# BOJ 9095: 1,2,3 더하기

# 디버그 함수 및 플래그 정의
DEBUG = False
def debug(*args):
    if DEBUG:
        print(*args)
        
# dp 배열 정의 (N < 11)
# dp[number] = number를 1,2,3의 합으로 나타내는 방법
# dp[number] = dp[number-1] + dp[number-2] + dp[number-3]
dp = [0] * 11

# 위 식의 index를 정상적으로 저장하기 위해, number>=3부터 시작해야 함.
dp[1] = 1 # 1은 1 한가지뿐
dp[2] = 2 # 2는 2, 1+1 두가지뿐
dp[3] = 4 # 3은 3, 2+1, 1+2, 1+1+1 네가지

# preprocess
for number in range(4, 11):
    dp[number] = dp[number-1] + dp[number-2] + dp[number-3]
    
# T 입력
T = int(input())

# 각 test case에 대해 iteration
for _ in range(T):
    N = int(input())
    # 미리 만들어둔 dp 배열 사용
    print(dp[N])