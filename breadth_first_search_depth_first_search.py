""" Breadth First Search and Depth First Search """
from collections import deque

def bfs(graph, root):
    """ Breadth First Search """
    visited = set()
    queue = deque([root])

    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


def dfs(graph, start, visited=None):
    """ Depth First Search """
    if visited is None:
        visited = set()
    visited.add(start)

    print(start, end=' ')

    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G'],
    'D': ['H', 'I'],
    'E': [],
    'F': ['J'],
    'G': [],
    'H': [],
    'I': [],
    'J': []
}

# Test the function with different starting nodes
print("BFS starting from node A:")
bfs(graph, 'A')
print("\n")

print("BFS starting from node B:")
bfs(graph, 'B')
print("\n")

print("BFS starting from node C:")
bfs(graph, 'C')
print("\n")


graph = {
    'A': set(['B', 'C', 'D']),
    'B': set(['E', 'F']),
    'C': set(['G']),
    'D': set(['H', 'I']),
    'E': set([]),
    'F': set(['J']),
    'G': set([]),
    'H': set([]),
    'I': set([]),
    'J': set([])
}

print("DFS starting from node A:")
dfs(graph, 'A')
print("\n")

print("DFS starting from node B:")
dfs(graph, 'B')
print("\n")

print("DFS starting from node C:")
dfs(graph, 'C')
print("\n")