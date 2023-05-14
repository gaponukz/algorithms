# https://www.eolymp.com/uk/submissions/13739052
import typing

T = typing.TypeVar('T', bound=typing.Hashable)

class Connectivity(typing.Generic[T]):
    def __init__(self):
        self.connections: dict[T, set[T]] = {}

    def add_connection(self, node1: T, node2: T):
        if node1 not in self.connections:
            self.connections[node1] = set()
        
        self.connections[node1].add(node2)
        
        if node2 not in self.connections:
            self.connections[node2] = set()
        
        self.connections[node2].add(node1)

    def remove_connection(self, node1: T, node2: T):
        if node1 in self.connections and node2 in self.connections[node1]:
            self.connections[node1].remove(node2)
            self.connections[node2].remove(node1)

    def get_connections(self, node) -> set[T]:
        if node in self.connections:
            return self.connections[node]
        
        else:
            return set()

def is_connected(graph: Connectivity[T]) -> bool:
    remaining = set(graph.connections)
    stack = [remaining.pop()]

    while stack:
        node = stack.pop()

        for neighbour in graph.get_connections(node):
            if neighbour in remaining:
                stack.append(neighbour)
                remaining.remove(neighbour)
        
    return len(remaining) == 0

if __name__ == "__main__":
    get_int_data = lambda: list(map(int, input().split()))
    n, m = get_int_data()

    graph = Connectivity[int]()
    ind_vertex = {}

    for i in range(m):
        a, b = get_int_data()
        graph.add_connection(a, b)
        ind_vertex[i + 1] = [a, b]
    
    k, = get_int_data()

    for _ in range(k):
        n, *vertexs = get_int_data()
        
        for i in vertexs:
            a, b = ind_vertex[i]
            graph.remove_connection(a, b)
        
        print("Connected" if is_connected(graph) else "Disconnected")

        for i in vertexs:
            a, b = ind_vertex[i]
            graph.add_connection(a, b)
