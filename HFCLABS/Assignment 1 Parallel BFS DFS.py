from multiprocessing import Process, Manager

def parallelBFS(graph, startNode, visited):
    queue = Manager().list()
    queue.append(startNode)
    visited[startNode] = True
 
    while queue:
        node = queue.pop(0)
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

def parallelDFS(graph, node, visited):
    visited[node] = True
 
    for neighbor in graph[node]:
        if not visited[neighbor]:
            parallelDFS(graph, neighbor, visited)

def main():
    # Get the number of nodes in the graph
    numNodes = int(input("Enter the number of nodes: "))
 
    # Create the graph as a dictionary of lists
    graph = {}
    for i in range(numNodes):
        graph[i] = []
 
    # Get the edges of the graph
    numEdges = int(input("Enter the number of edges: "))
    for i in range(numEdges):
        node1, node2 = map(int, input("Enter an edge (node1 node2): ").split())
        graph[node1].append(node2)
        graph[node2].append(node1)
 
    # Get the starting node for the search
    startNode = int(input("Enter the starting node: "))
 
    # Create the shared visited array
    manager = Manager()
    visited = manager.list([False] * numNodes)
 
    # Choose the search type (BFS or DFS)
    searchType = int(input("Enter 1 for BFS or 2 for DFS: "))
    if searchType == 1:
        # Perform parallel BFS
        p = Process(target=parallelBFS, args=(graph, startNode, visited))
        p.start()
        p.join()
    else:
        # Perform parallel DFS
        p = Process(target=parallelDFS, args=(graph, startNode, visited))
        p.start()
        p.join()
 
    # Print the visited nodes
    print("Visited nodes:", [i for i, v in enumerate(visited) if v])

if __name__ == '__main__':
    main()


# Sample input
# Enter the number of nodes: 5
# Enter the number of edges: 5
# Enter an edge (node1 node2): 0 1
# Enter an edge (node1 node2): 0 2
# Enter an edge (node1 node2): 1 2
# Enter an edge (node1 node2): 2 3
# Enter an edge (node1 node2): 3 4
# Enter the starting node: 0
# Enter 1 for BFS or 2 for DFS: 1