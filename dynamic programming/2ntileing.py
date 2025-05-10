# BOJ 11726: 2*n 타일링

# 디버그 함수 및 플래그 정의
DEBUG = False
def debug(*args):
    if DEBUG:
        print(*args)
        
# n 입력
n = int(input())

# n 크기에 따른 dp 배열 동적 생성 (n <= 1000)
# dp 배열 정의 
# dp[size] = 2*size 크기의 직사각형을 1*2, 2*1로 채우는 방법 수
# 초기항을 써서 규칙을 찾아봅시다
# dp[1] = 1, 2*1 하나밖에 없음
# dp[2] = 2, 2*1 두개, 1*2 두개
# 모든 경우를 세로칸 한개와 가로칸 두개의 조합으로 나타낼 수 있음
# 따라서 이전의 최적해 경우의 수는 세로칸 한개 혹은 가로칸 두개의 경우의 수의 합으로 표현 가능
# dp[size] = dp[size-1] + dp[size-2]
# 한편, 합동식의 분배법칙에 의해 dp[size] % 10007 = (dp[size-1] + dp[size-2]) % 10007이 성립
# int64 size를 넘어서지 않게 미리미리 처리해주자
dp = [0] * 1001

# dp 초기값 설정
dp[1] = 1
dp[2] = 2

# dp 실행
for size in range(3, n+1):
    dp[size] = (dp[size-1] + dp[size-2]) % 10007

# 결과값 출력
print(dp[n])