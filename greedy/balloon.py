# n이 100만이다. 일단 nlogn~n 속도 안에 풀어야겠지? 적은 시간에 구현 가능한 간단한 알고리즘을 생각해보면 될 것 같은데...
# 테스트 케이스 2번에 값들이 전부 음수값만 나온걸 보면 어떤 패턴을 확인할 수 있는 것 같다.
# 즉, 적어도 답으로 골라야 하는 값들은 작은 값들일것이다.(큰 값은 제외해야 한다)
# 좌우 비교 연산을 한다는 점에 착안하여 문제를 해결해보자.
def solution(a):
    answer = 0
    data_size = len(a)
    inf = 1000000000 + 1 # 최소값 설정의 초기값    

    # 초기 값은 뭐 들어가도 상관없으니까 좋아하는 숫자 넣음
    magic_number = 119

    left_min = [magic_number]*data_size
    right_min = [magic_number]*data_size

    # 좌->우로 가면서 그 값보다 작은 값들 순회
    real_min = inf # 전체 배열 중 가장 최소값
    for i in range(data_size):
        real_min = min(real_min, a[i])
        left_min[i] = real_min

    # 우->좌로 가면서 그 값보다 작은 값들 순회
    real_min = inf
    for i in range(data_size-1, -1, -1):
        real_min = min(real_min, a[i])
        right_min[i] = real_min


    for i in range(data_size):
        if a[i] <= left_min[i] or a[i] <= right_min[i]:
            answer += 1
    return answer
