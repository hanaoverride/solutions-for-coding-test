# BOJ 2231번: 분해합
# 디버그 함수 및 플래그 정의
DEBUG = False
def debug(*args):
    if DEBUG:
        print(*args)
        
# 999999의 분해합을 생각해보자. 999999 + 9*6으로, 원래 수를 제외한 분해합이 아무리 커도 9*6=54를 넘지 못한다.
# 마찬가지로 99999의 분해합을 생각해도 99999 + 9*5로, 원래 수를 제외한 분해합이 아무리 커도 9*5= 45를 넘지 못한다.
# 9의 분해합을 생각해보면 9 + 9 = 18.
# 즉 1 <= N <= 1000000의 경우에서 생성자는 두 자리수 이상 차이나지 않으므로,
# 최고차항 자리수가 1인 경우  N자리수의 생성자를 찾는다면 N자리부터,
# 그 이외의 경우  N자리수의 생성자를 찾는다면 N-1자리부터 찾으면 된다.

# N 입력
N = int(input())


base = len(str(N))

# 숫자를 저장할 칸
numberset = [0] * base
# 최소값 변수
result = 9999999
# 브루트포스 함수 정의
def b_force(n_set, current_pointer):
    global result
    debug(n_set)
    # 수를 완성했다면
    if current_pointer == base:
        concat_number = int(''.join(map(str, n_set)))
        init = concat_number + sum(n_set)
        # 생성자 조건 체크
        if init == N:
            result = min(result, concat_number)
        return
    # 각 경우 탐색
    for i in range(0,10):
        n_set[current_pointer] = i
        b_force(n_set, current_pointer + 1)

# 브루트포스 함수 호출
b_force(numberset, 0)

# 결과 출력
print(result if result != 9999999 else 0)

