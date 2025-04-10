# 프로그래머스 레벨 2: 기능개발
from math import ceil

def solution(progresses, speeds):
    # 정답 배열에는 최대값이 갱신되기 전까지의 값의 갯수를 구한다.
    answer = []
    # 각 필요한 기간을 배열로 선정
    mandate = [ceil((100 - progresses[i]) / speeds[i]) for i in range(len(progresses))]
    
    # 초기 카운트값
    count = 1
    # 초기 최대값
    cur_max = -1
    # 악명높은 O(n) 탐색
    for val in mandate:
        # 최대값이 갱신되는 경우, 뒤의 작업은 앞의 작업보다 무조건 더 많이 걸릴것이다.
        # 따라서 최대값 이전에 작업중이던 모든 작업을 commit 한다.
        if cur_max < val:
            cur_max = val
            answer.append(count)
            count = 1
        # 앞의 기간보다 짧게 끝나는 작업은 commit하지 않고 긴 작업이 끝날때까지 기다린다.
        else:
            count += 1
    # 마지막 경우는 최대값을 갱신하지 않으므로 리스트에 append 한다.
    answer.append(count)
    # 첫 값의 경우는 -1 작업이 더미 작업이므로 제외하고 계산한다.
    return answer[1:]