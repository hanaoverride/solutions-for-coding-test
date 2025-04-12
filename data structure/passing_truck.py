# 프로그래머스 레벨 2: 다리를 지나는 트럭
def solution(bridge_length, weight, truck_weights):
    # 최초 시작 시간은 0
    time = 0
    # 현재 올라가있는 트럭
    current_truck = []
    sum_truck = 0
    
    while truck_weights or current_truck:
        time += 1

        # 먼저 트럭들이 1씩 전진한다
        for truck in current_truck:
            truck[0] += 1

        # 다 건넌 트럭을 제거 (여러 대도 한꺼번에 처리)
        while current_truck and current_truck[0][0] >= bridge_length:
            left_truck = current_truck.pop(0)
            sum_truck -= left_truck[1]

        # 올릴 수 있으면 트럭 올리기
        if truck_weights and sum_truck + truck_weights[0] <= weight:
            # index 0은 다리 위에 있는 시간, index 1은 트럭의 무게
            new_truck = [0, truck_weights.pop(0)]
            current_truck.append(new_truck)
            sum_truck += new_truck[1]
    return time