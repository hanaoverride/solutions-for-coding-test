# 프로그래머스 레벨 2: 타겟 넘버
# 2^20 = 1024*1024 ~ 1000000
from collections import deque
def solution(numbers, target):
    # 큐 선언
    q = deque()
    answer = 0

    # 길이 계산
    length = len(numbers)

    # 첫 항 덧셈과 뺄셈에 대한 탐색 시작
    # (addition, sum, next_iter)
    q.append((numbers[0], 0, 1))
    q.append((-numbers[0], 0, 1))

    # 완전 탐색
    while q:
        get_tuple = q.popleft()
        sum = get_tuple[0] + get_tuple[1]
        curr_iter = get_tuple[2]

        # 탐색 한계점 체크
        if curr_iter == length:
            # 탐색 결과가 일치한다면
            if sum == target:
                answer += 1
            continue
        # 덧셈 튜플 생성
        new_tuple_plus = (numbers[curr_iter], sum, curr_iter + 1)
        # 뺄셈 튜플 생성
        new_tuple_minus = (-numbers[curr_iter], sum, curr_iter + 1)

        # 큐 삽임
        q.append(new_tuple_plus)
        q.append(new_tuple_minus)

    return answer