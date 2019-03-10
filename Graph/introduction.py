graph = {}
node = int(raw_input())
edges = int(raw_input())
visited = [False] * 10000 # visited node


def dfs(node):
    """Depth First Search"""
    print node ,
    visited[node] = True
    for each in graph[node]:
        if not visited[each]:
            dfs(each)

for each in range(0, edges):
    l = [int(k) for k in raw_input().split()]
    u = l[0]
    v = l[1]
    if not (u in graph):
        graph[u] = []
    graph[u].append(v)

print graph
dfs(1)
