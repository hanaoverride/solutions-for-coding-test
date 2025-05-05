import heapq

# 프로그래머스 레벨 2: 더 맵게
def solution(scoville, K):
    answer = 0
    # 최소 힙 활용
    min_heap = []

    # 모든 값을 힙에 넣어 힙 트리 완성
    heapq.heapify(scoville)

    # 모든 값이 K 이상이 될때까지(그리고 힙의 자손이 남아있을때까지)
    while scoville[0] < K and len(scoville) >= 2:
        # 공식에 따라 값을 두개 pop 해서 새 값을 만듦
        least_hot = heapq.heappop(scoville)
        sleast_hot = heapq.heappop(scoville)
        newval = least_hot + 2 * sleast_hot

        # 새 값을 다시 최소 힙에 삽입
        heapq.heappush(scoville, newval)
        # 조합 회수 증가
        answer += 1

    if len(scoville) < 2 and scoville[0] < K:
        return -1
    return answer

