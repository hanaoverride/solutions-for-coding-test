# BOJ 2579: 계단 오르기

# 디버그 함수 및 플래그 정의
DEBUG = False
def debug(*args):
    if DEBUG:
        print(*args)
        
# 계단의 갯수 입력
number_of_stairs = int(input())

# 계단 갯수에 따른 배열 생성
stairs = [0] * (number_of_stairs + 1)

# iteration에 따른 각 계단 값 입력
for i in range(1, number_of_stairs + 1):
    value = int(input())
    debug("value: " + str(value))
    stairs[i] = value
    debug("stairs[i]: " + str(stairs[i]))

debug(stairs)

# dp 배열 동적 생성 size = number_of_stairs
dp = [-1] * (number_of_stairs + 1)

# 최적값이 "3연속 1칸 금지"를 언급하고 있으므로, 현재의 상태를 함께 저장할 시스템이 필요함
# 그것을 위해 dfs를 dp와 함께 사용함

# DFS(curr_state): 현재 단계수를 저장하는 DFS 함수
def DFS(curr_state):
    # 초기값 정의: 0, 1, 2
    if curr_state == 0:
        return 0
    elif curr_state == 1:
        return stairs[1]
    elif curr_state == 2:
        return stairs[1] + stairs[2]
    elif dp[curr_state] != -1:
        return dp[curr_state]
    
    # curr_state > 2인 경우, 재귀 호출을 통한 dp값 계산 필요
    # 현재 시점에서 연속된 칸의 갯수가 몇개인지 알 수 있는 방법이 없다.
    # (물론 연속된 칸의 갯수를 함께 저장해 DFS를 하는 방법이 있지만 계산량이 더 많아질것이다.)
    # 이를 극복하기 위해, 그냥 두칸을 뛰어넘어버리면 1을 건너뛸 수 있는 횟수가 초기화된다. 간단하네요!
    dp[curr_state] = max(
        # case 1: 두칸 뛰어넘고 끝.(연속된 칸의 갯수 1)
        DFS(curr_state - 2) + stairs[curr_state],
        # case 2: 두칸 뛰어넘고, 한칸 더 뛰어넘고.(연속된 칸의 갯수 2)
        # 이 이상은 연속된 칸의 갯수가 3 이상이 되어버리므로, 불가능.
        DFS(curr_state - 3) + stairs[curr_state - 1] + stairs[curr_state]
        )
    
    # dp 값을 성공적으로 계산했다면, 반환해야겠지?
    return dp[curr_state]

# 목표 dp값을 기반으로 한 dfs+dp 호출
print(DFS(number_of_stairs))