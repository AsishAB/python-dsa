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

# Graph with weighted and directed weights
class Graph2:
    def __init__(self, num_nodes, edges, directed=False, weighted=False):
        self.num_nodes = num_nodes
        self.directed = directed
        self.weighted = weighted
        self.data = [[] for _ in range(num_nodes)]
        self.weight = [[] for _ in range(num_nodes)]
        for edge in edges:
            if self.weighted:
                node1, node2, weight = edge
                self.data[node1].append(node2)
                self.weight[node1].append(weight)
                if not directed:
                    self.data[node2].append(node1)
                    self.weight[node2].append(weight)
                else:
                    node1, node2 = edge
                    self.data[node1].append(node2)
                    if not directed:
                        self.data[node2].append(node1)
    
    def __repr__(self):
        result = ""
        if self.weighted:
            for i, (nodes, weights) in  enumerate(list(zip(self.data, self.weight))):
                result += f"{i}: {list(zip(nodes, weights))}\n"
        else:
            for i, nodes in enumerate(self.data):
                result += f"{i}: {nodes}\n"

        return result

num_nodes2 = 9
edges2 = [(0,1,3), (0,3,2),(0,8,4),(1,7,4), (2,7,2), (2,3,6), (2,5,1), (3,4,1), (4,8,8), (5,6,8)]

graph2 = Graph2(num_nodes2, edges2, weighted=True)

print(f"Graph 2 =\n {graph2}")

# Find the shortest path of a graph

def shortest_path(graph, source, target):
    visited = [False] * len(graph.data)
    distance = [float('inf')] * len(graph.data)
    queue = []
    distance[source] = []
    queue.append(source)
    idx = 0
    while idx < len(queue) and not visited[target]:
        current = queue[idx]
        idx += 1
        update_distances(graph, current, distance)
        next_node = pick_next_node(distance, visited)
        if next_node:
            queue.append(next_node)

        visited[current] = True

    return distance[target]

def update_distances(graph, current, distance, parent=None):
    # Update the distance of current node's neighbours
    neighbours = graph.data[current]
    weights = graph.weight[current]
    for i, node in enumerate(neighbours):
        weight = weights[i]
        if distance[current] + weight < distance[node]:
            distance[node] = distance[current] + weight
            if parent:
                parent[node] = current
    

def pick_next_node(distance, visited):
    # Pick the next unvisited node at the smallest distance
    min_distance = float('inf')
    min_node = None
    for node in range(len(distance)):
        if not visited[node] and distance[node] < min_distance:
            min_node = node
            min_distance = distance[node]
    return min_node

        




