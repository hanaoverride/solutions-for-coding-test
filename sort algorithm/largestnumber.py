# 프로그래머스 레벨 2: 가장 큰 수
def solution(numbers):
    answer = ''
    # 람다식을 이용해 사전순을 기준으로 내림차순 정렬
    # 모든 자릿수를 비교하기 위해 모든 수를 3배 길이 한다
    # (수의 한계가 1000인데 3자리까지만 하면 되므로)
    numbers.sort(key=lambda x: str(x)*3, reverse=True)
    
    # 모든 수가 0일 경우
    if numbers[0] == 0:
        return "0"
    
    # 자리수가 높은것부터 차례로 이어붙이면, 그게 가장 큰 수
    for number in numbers:
        answer += str(number)
        
    return answer