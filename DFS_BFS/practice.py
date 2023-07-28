'''
#####################
#     BFS, DFS      #
# BFS: 너비 우선 탐색, 그래프에서 가까운 노드부터 우선적으로 탐색하는 알고리즘
#####################
'''
# 위에서 아래로, 왼쪽부터 작성 (연결되어 있는 노드들 작성)
def bfs(graph, start_node):
    visit = list()
    queue = list()

    queue.append(start_node)

    while queue:
        node = queue.pop(0) # pop(0)이면 앞에꺼 빠짐, pop()이면 뒤에꺼가 빠짐
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])

    return visit


def dfs(graph, start_node):
    visit = list()
    stack = list()

    stack.append(start_node)

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])

    return visit


if __name__ == "__main__":
    graph = {
        'A': ['B'],
        'B': ['A', 'C', 'H'],
        'C': ['B', 'D'],
        'D': ['C', 'E', 'G'],
        'E': ['D', 'F'],
        'F': ['E'],
        'G': ['D'],
        'H': ['B', 'I', 'J', 'M'],
        'I': ['H'],
        'J': ['H', 'K'],
        'K': ['J', 'L'],
        'L': ['K'],
        'M': ['H']
    }

    print(bfs(graph, 'A'))
    print(dfs(graph, 'A'))