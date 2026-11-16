# Dijkstra's Shortest Path Algorithm

n = int(input("Enter number of vertices: "))

print("Enter cost matrix (-1 for no connection):")

graph = []

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

source = int(input("Enter source vertex (0 to n-1): "))

dist = [float('inf')] * n
visited = [False] * n

dist[source] = 0

for i in range(n):

    # Find the nearest unvisited vertex
    min_dist = float('inf')
    u = -1

    for j in range(n):
        if not visited[j] and dist[j] < min_dist:
            min_dist = dist[j]
            u = j

    if u == -1:
        break

    visited[u] = True

    # Update distances of adjacent vertices
    for v in range(n):
        if graph[u][v] >= 0 and not visited[v]:
            if dist[u] + graph[u][v] < dist[v]:
                dist[v] = dist[u] + graph[u][v]

print("\nShortest distances from source vertex", source)

for i in range(n):
    if dist[i] == float('inf'):
        print("Vertex", i, ": Not reachable")
    else:
        print("Vertex", i, ":", dist[i])