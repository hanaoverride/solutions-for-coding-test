def solution(n, computers):
    # 연결 완료한 리스트는 여기다 만들기
    complete_graph = []

    # 무슨 탐색을 할지 모르겠는데, 일단 DFS로 해보죠?
    def DFS(start_node): # 재귀호출은 안좋을거같아 ㅠㅠ stack 구조로 작성해보자
        stack = []
        visited = [] # 방문한 노드는 대충 여기다 체크
        # 탐색 시작점 push
        stack.append(start_node)
        while stack:
            # 탐색 중인 노드
            curr_node = stack.pop()
            # 탐색한 곳을 또 탐색할 필요는 없다.
            if curr_node in visited:
                continue
            # 현재 노드를 탐색함으로 둔다.
            visited.append(curr_node)
            for adj_node in range(len(computers[curr_node])):
                if computers[curr_node][adj_node] == 1:
                    print(adj_node)
                    stack.append(adj_node)
        complete_graph.append(visited)
        print(complete_graph)
    answer = 0
    # 각 정점에 대해 DFS를 돌리자
    for node in range(n):
        flag = True
        for individual_graph in complete_graph:
            if node in individual_graph:
                flag = False
                break
        if flag:
            print("Flag activated in node" + str(node))
            DFS(node)
    answer = len(complete_graph)
    return answer
