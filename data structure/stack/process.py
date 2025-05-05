# 프로그래머스 레벨 2: 프로세스
def solution(priorities, location):
    # 완료 순서 배열을 정의한다
    order = []
    # 0번부터 n번 프로세스까지 인덱싱
    process_number = [i for i in range(len(priorities))]

    # 요소가 하나만 남으면 무조건 바로 실행하므로 그때까지 반복
    while len(priorities) > 1:
        # 후행하는 요소 중 우선순위가 높은 요소가 있을 경우 좌 원소를 우측에 부착
        if priorities[0] < max(priorities[1:]):
            process_number.append(process_number.pop(0))
            priorities.append(priorities.pop(0))
        # 없으면 가장 우선순위가 높다는 뜻, 완료 순서에 부착한다
        else:
            order.append(process_number.pop(0))
            priorities.pop(0)
    # 1번째부터 시작
    count = 1
    # 프로세스 id는 몇번째?
    for pid in order:
        if pid == location:
            break
        count += 1
    return count

