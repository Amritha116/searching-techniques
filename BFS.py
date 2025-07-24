# Input Graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'E'],
    'D': ['B', 'E'],
    'E': ['C', 'D']
}

# Function for BFS
def bfs(visited, graph, start_node):
    visited = []
    queue = []

    visited.append(start_node)
    queue.append(start_node)

    print("\nRESULT:")

    while queue:
        s = queue.pop(0)
        print(s, end=" ")

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

# Main Code
snode = input("Enter Starting Node (A, B, C, D, or E): ").upper()
bfs([], graph, snode)
