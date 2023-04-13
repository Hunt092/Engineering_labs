class Graph:
    def __init__(self):
        self.visited = {}
        self.adj = {}

    def addEdge(self, start, end):
        try:
            self.adj[start].append(end)
        except:
            self.adj[start] = [end]
        finally:
            self.visited[start] = False

    def DFS(self, node):
        self.visited[node] = True
        print(node, end=" ")
        for i in self.adj[node]:
            if not self.visited[i]:
                self.DFS(i)

    def BFS(self, node):
        queue = []
        self.visited[node] = True
        queue.append(node)
        while queue:
            cur = queue[0]
            print(cur)
            del queue[0]
            for i in self.adj[cur]:
                if not self.visited[i]:
                    self.visited[i] = True
                    queue.append(i)


if __name__ == "__main__":

    g = Graph()

    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    g = Graph()

    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    g.BFS(2)
