class Graph:
    def __init__(self):
        self._data = {}

    def addVertex(self, key):
        if key not in self._data:
            self._data[key] = set()

    def vertex(self):
        print("\nSeluruh Node = ", end="")
        for key, value in self._data.items():
            print(key, end=' ')
        print()

    def edge(self):
        print("Seluruh Edge = ", end="")
        listEdge = set()
        for key, value in self._data.items():
            for item in self._data[key]:
                if key + item not in listEdge and item + key not in listEdge:
                    listEdge.add(key + item)
        for item in listEdge:
            print(item, end=' ')
        print()

    def addEdge(self, x, y):
        if x in self._data and y in self._data:
            self._data[x].add(y)
            self._data[y].add(x)

    def bfs(self, node):
        print("Traversing BFS = ", end="")
        visited = []
        listQueue = []
        visited.append(node)
        listQueue.append(node)

        while listQueue:
            n = listQueue.pop(0)
            for item in self._data[n]:
                if item not in visited:
                    visited.append(item)
                    listQueue.append(item)
            print(n, end=' ')
        print("\n")


graph = Graph()
graph.addVertex('a')
graph.addVertex('b')
graph.addVertex('c')
graph.addVertex('d')
graph.addVertex('e')
graph.addVertex('f')
graph.addVertex('g')

graph.addEdge('a', 'b')
graph.addEdge('b', 'c')
graph.addEdge('b', 'd')
graph.addEdge('c', 'g')
graph.addEdge('c', 'e')
graph.addEdge('d', 'e')
graph.addEdge('f', 'e')

graph.vertex()
graph.edge()
graph.bfs("a")