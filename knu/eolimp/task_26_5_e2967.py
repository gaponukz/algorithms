# https://www.eolymp.com/uk/submissions/13793107
import math
import heapq
import typing
import dataclasses

T = typing.TypeVar('T', bound=typing.Hashable)

class Graph(typing.Generic[T]):
    def __init__(self):
        self._vertices: dict[T, dict[T, float]] = {}

    def add_vertex(self, vertex: T):
        self._vertices[vertex] = {}

    def add_edge(self, start: T, end: T, cost: float):
        self._vertices[start][end] = cost

    def get_neighbors(self, vertex) -> dict[T, float]:
        return self._vertices[vertex]

    def get_vertices(self) -> list[T]:
        return list(self._vertices)

@dataclasses.dataclass
class PrimResult(typing.Generic[T]):
    source: T
    destination: T
    cost: float

def prim(graph: Graph[T]) -> list[PrimResult[T]]:
    start_vertex = graph.get_vertices()[0]
    visited = {start_vertex}
    minimum_spanning_tree = []
    heap = []

    for neighbor, cost in graph.get_neighbors(start_vertex).items():
        heapq.heappush(heap, (cost, start_vertex, neighbor))

    while heap:
        cost, source, destination = heapq.heappop(heap)

        if destination not in visited:
            visited.add(destination)
            minimum_spanning_tree.append(PrimResult(source, destination, cost))

            for neighbor, cost in graph.get_neighbors(destination).items():
                heapq.heappush(heap, (cost, destination, neighbor))

    return minimum_spanning_tree

def calculate_distance(x1: float, y1: float, x2: float, y2: float) -> float:
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

if __name__ == '__main__':
    graph = Graph[int]()
    coordinates: dict[int, tuple[int, int]] = {}

    n = int(input())

    for i in range(n):
        graph.add_vertex(i)
        a, b = list(map(int, input().split()))
        coordinates[i] = (a, b)

    for coord1, (x1, y1) in coordinates.items():
        for coord2, (x2, y2) in coordinates.items():
            if coord1 != coord2:
                distance = calculate_distance(x1, y1, x2, y2)
                graph.add_edge(coord1, coord2, distance)

    prim_result = prim(graph)
    
    print(round(sum(item.cost for item in prim_result), 10))
