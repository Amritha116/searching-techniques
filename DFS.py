# Input Graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'E'],
    'D': ['B', 'E'],
    'E': ['C', 'D']
}

# List used to store visited nodes
visitedNodes = []

# DFS function
def dfs(visitedNodes, graph, node):
    if node not in visitedNodes:
        print(node, end=" ")
        visitedNodes.append(node)
        for neighbour in graph[node]:
            dfs(visitedNodes, graph, neighbour)

# Driver Code
snode = input("Enter Starting Node (A, B, C, D, or E): ").upper()
print("RESULT :")
print("-" * 20)
dfs(visitedNodes, graph, snode)