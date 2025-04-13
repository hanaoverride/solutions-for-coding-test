# 프로그래머스 레벨 2: 전화번호 목록
# suggestion : O(n) ~ O(n log n)(since n = 1000000)
def solution(phone_book):
    # 전화번호부를 사전순 정렬(어차피 뒤에만 나옴 ㅋ)
    phone_book.sort()
    
    # n-1번째 전화번호까지 비교
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False
    return True