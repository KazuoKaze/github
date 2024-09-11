

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = [[] for _ in range(num_vertices)]

    def add_edge(self, src, dest):
        self.graph[src].append(dest)
        self.graph[dest].append(src)

    def display(self):
        for row in self.graph:
            print(row)

    def connected_components(self):
        visited = [False] * self.num_vertices
        componenets = []
        for v in range(self.num_vertices):
            if not visited[v]:
                component = []
                self._connected_components(v, visited, component)
                componenets.append(component)
        return componenets

    def _connected_components(self, v, visited, component):
        visited[v] = True
        component.append(v)
        for ngh in self.graph[v]:
            if not visited[ngh]:
                self._connected_components(ngh, visited, component)


graph = Graph(6)
## BFS:
graph = Graph(6)
graph.add_edge(0, 1)
graph.add_edge(2, 3)
graph.add_edge(4, 5)
print(graph.connected_components())  # Output: [[0, 1], [2, 3], [4, 5]]
