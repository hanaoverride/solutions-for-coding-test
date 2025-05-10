# BOJ 12865: 평범한 배낭

# 디버그 함수 및 플래그 정의
DEBUG = True
def debug(*args):
    if DEBUG:
        print(*args)
        
# dp 배열 정의 (N = 100, K = 100000)
# dp[item][cap] = item번째 아이템까지 택했을때 최대치가 cap일때의 최적(최대) 무게
dp = [[0] * 100001 for _ in range(101)]

# 무게 저장 배열 정의(N = 100, as tuple)
obj = [None] * 101

# N, K 입력
N, K = map(int, input().split())

# 각 case에 대해 W, V iteration
for i in range(1, N + 1):
    W, V = map(int, input().split())
    obj[i] = (W, V)

# DP 실행
# 계산을 어떻게 할것인가? N번째 아이템까지 택했을때의 최적해를 저장하고 갱신한다...
# 현재 item이 cap을 초과하는 경우, 갱신할 수 없다. 따라서 이전 선택지까지의 최적해를 불러오고 
# (if weight > cap: dp[item][cap] = dp[item-1][cap]  )
# 그렇지 않은 경우? 새 아이템을 넣어보고 그것이 이전 선택지까지의 최적해와 큰지를 비교한다...
# (dp[item][cap] = max(dp[item-1][cap], dp[item-1][cap-weight] + value))
# 1번째 아이템부터 N번째 아이템까지
for item in range(1, N + 1):
    # 무게 cap이 1부터 K(최대치) 까지
    for cap in range(1, K + 1):
        weight, value = obj[item]
        if weight > cap:
            dp[item][cap] = dp[item-1][cap]
        else:
            dp[item][cap] = max(dp[item-1][cap], dp[item-1][cap-weight] + value)

# 결과: dp 계산 결과 출력
print(dp[N][K])
