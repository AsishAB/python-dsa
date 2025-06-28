# Define a Graph class to maintain the adjacancy list

num_nodes = 5
edges = [(0,1), (0,4), (1,2), (1,3), (1,4), (2,3), (3,4)]

# enumerate function - > Creates a key-value pair from an array

class Graph:
    def __init__(self, num_nodes , edges ):
        self.num_nodes = num_nodes
        self.data = [[] for _ in range(num_nodes)] # [] * num_nodes is not suitable here, as [] is not copied multiple times. So, changing one of the [] with an append will change all the empty lists. Google it for clarification
        for n1, n2 in edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)
    def __repr__(self):
        return "\n".join([f"{node}: {neighbours}" for node, neighbours in enumerate(self.data)])
    
    def __str__(self):
        return self.__repr__()

graph1 = Graph(num_nodes, edges)
print(graph1)
# graph1

# print([f"{node}: {neighbours}" for node, neighbours in enumerate(graph1.data)])

# Breadth First Search for a Graph

def bfs(graph, root):
    queue = [] # A FIFO QUEUE
    discovered = [False] * len(graph.data)
    discovered[root] = True
    distance = [None] * len(graph.data) # Distance = Number of edges
    queue.append(root) # This is also called en-queue
    distance[root] = 0
    parent = [None] * len(graph.data)

    idx = 0 
    while idx < len(queue):
        # Python does not have a de-queue functionality. So, use this
        current = queue[idx]
        idx += 1

        # Check all edges of the current
        for node in graph.data[current]:
            if not discovered[node]:
                distance[node] = 1 + distance[current]
                parent[node] = current
                discovered[node] = True
                queue.append(node)

    # distance is the value of the index in queue
    # For example , distance of the node 3, is available in distance[3], which is 0

    return queue, distance, parent


print(bfs(graph1, 3))

# Depth First Search (check it again)

def dps(graph, root):
    stack = []
    discovered = [False] * len(graph.data)
    result = []
    stack.append(root)
    while len(stack) > 0:
        current = stack.pop()
        if not discovered[current]:
            discovered[current] = True
        result.append(current)
        for node in graph.data[current]:
            if not discovered[node]:
                stack.append(node)
    return result