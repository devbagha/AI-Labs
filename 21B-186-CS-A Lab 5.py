##################TASK 1 ##################################
# A Node class for GBFS Pathfinding
class Node:
    def __init__(self, v, weight):
        self.v = v
        self.weight = weight

# pathNode class will help to store
# the path from src to dest.
class PathNode:
    def __init__(self, node, parent):
        self.node = node
        self.parent = parent

# Function to add edge in the graph.
def addEdge(u, v, weight):
    # Add edge u -> v with weight weight.
    adj[u].append(Node(v, weight))

# Declaring the adjacency list
adj = {}

# Greedy best first search algorithm function
def GBFS(h, src, dest):
    """ 
    This function returns a list of 
    integers that denote the shortest
    path found using the GBFS algorithm.
    If no path exists from src to dest, we will return an empty list.
    """
    # Initializing openList and closeList.
    openList = []
    closeList = []

    # Inserting src in openList.
    openList.append(PathNode(src, None))

    # Iterating while the openList 
    # is not empty.
    while openList:
        currentNode = openList[0]
        currentIndex = 0
        
        # Finding the node with the least 'h' value
        for i in range(len(openList)):
            if h[openList[i].node] < h[currentNode.node]:
                currentNode = openList[i]
                currentIndex = i

        # Removing the currentNode from 
        # the openList and adding it in 
        # the closeList.
        openList.pop(currentIndex)
        closeList.append(currentNode)
        
        # If we have reached the destination node.
        if currentNode.node == dest:
            # Initializing the 'path' list. 
            path = []
            cur = currentNode

            # Adding all the nodes in the 
            # path list through which we have
            # reached to dest.
            while cur is not None:
                path.append(cur.node)
                cur = cur.parent
            
            # Reversing the path, because
            # currently it denotes path
            # from dest to src.
            path.reverse()
            return path

        # Iterating over adjacents of 'currentNode'
        # and adding them to openList if 
        # they are neither in openList or closeList.
        for node in adj[currentNode.node]:
            if not any(x.node == node.v for x in openList) and not any(x.node == node.v for x in closeList):
                openList.append(PathNode(node.v, currentNode))

    return []

# Driver Code
""" Making the following graph
'A': {'B':9, 'C':4, 'D':7}
'B': {'A':9, 'E':11}
'C': {'A':4, 'E':17, 'F':12}
'D': {'A':7, 'F':14}
'E': {'B':11, 'C':17, 'Z': 5}
'F': {'C':12, 'D':14, 'Z': 9}
"""
# Initializing the adjacency list
adj = {
    'A': [],
    'B': [],
    'C': [],
    'D': [],
    'E': [],
    'F': [],
    'Z': []
}

# Adding edges with corresponding weights
addEdge('A', 'B', 9)
addEdge('A', 'C', 4)
addEdge('A', 'D', 7)
addEdge('B', 'A', 9)
addEdge('B', 'E', 11)
addEdge('C', 'A', 4)
addEdge('C', 'E', 17)
addEdge('C', 'F', 12)
addEdge('D', 'A', 7)
addEdge('D', 'F', 14)
addEdge('E', 'B', 11)
addEdge('E', 'C', 17)
addEdge('E', 'Z', 5)
addEdge('F', 'C', 12)
addEdge('F', 'D', 14)
addEdge('F', 'Z', 9)

# Defining the heuristic values for each node.
h = {'A': 21, 'B': 14, 'C': 18, 'D': 18, 'E': 5, 'F': 8, 'Z': 0}

# Finding the shortest path using GBFS
path = GBFS(h, 'A', 'Z')

# Printing the shortest path
for i in range(len(path) - 1):
    print(path[i], end=" -> ")
print(path[len(path)-1])
#######################TASK 2 ##########################
import heapq

# A Node class for Uniform Cost Search
class Node:
    def __init__(self, v, weight):
        self.v = v
        self.weight = weight

# Function to add edge in the graph.
def addEdge(u, v, weight):
    # Add edge u -> v with weight weight.
    adj[u].append(Node(v, weight))

# Uniform Cost Search algorithm function
def UCS(src, dest):
    # Initializing the priority queue (frontier)
    frontier = [(0, src)]
    # Initializing the set of explored nodes
    explored = set()

    # Iterating until the frontier is empty
    while frontier:
        # Pop the node with the minimum cost from the frontier
        cost, node = heapq.heappop(frontier)

        # If the node is the destination, return the cost
        if node == dest:
            return cost

        # Add the node to the explored set
        explored.add(node)

        # Iterate over the neighbors of the current node
        for neighbor in adj[node]:
            # If the neighbor has not been explored
            if neighbor.v not in explored:
                # Calculate the new cost
                new_cost = cost + neighbor.weight
                # Add the neighbor to the frontier with its cost
                heapq.heappush(frontier, (new_cost, neighbor.v))

    # If no path is found, return infinity
    return float('inf')

# Driver Code
""" Making the following graph
'A': {'B':9, 'C':4, 'D':7}
'B': {'A':9, 'E':11}
'C': {'A':4, 'E':17, 'F':12}
'D': {'A':7, 'F':14}
'E': {'B':11, 'C':17, 'Z': 5}
'F': {'C':12, 'D':14, 'Z': 9}
"""
# Initializing the adjacency list
adj = {
    'A': [],
    'B': [],
    'C': [],
    'D': [],
    'E': [],
    'F': [],
    'Z': []
}

# Adding edges with corresponding weights
addEdge('A', 'B', 9)
addEdge('A', 'C', 4)
addEdge('A', 'D', 7)
addEdge('B', 'A', 9)
addEdge('B', 'E', 11)
addEdge('C', 'A', 4)
addEdge('C', 'E', 17)
addEdge('C', 'F', 12)
addEdge('D', 'A', 7)
addEdge('D', 'F', 14)
addEdge('E', 'B', 11)
addEdge('E', 'C', 17)
addEdge('E', 'Z', 5)
addEdge('F', 'C', 12)
addEdge('F', 'D', 14)
addEdge('F', 'Z', 9)

# Finding the shortest path cost using UCS
cost = UCS('A', 'Z')

# Printing the shortest path cost
print("Uniform Cost Search Cost:", cost)
#######################TASK 3 #################################
import heapq

# A Node class for A* Search
class Node:
    def __init__(self, v, weight):
        self.v = v
        self.weight = weight

# Function to add edge in the graph.
def addEdge(u, v, weight):
    # Add edge u -> v with weight weight.
    adj[u].append(Node(v, weight))

# A* Search algorithm function
def AStar(src, dest, heuristic):
    # Initializing the priority queue (frontier)
    frontier = [(0 + heuristic[src], 0, src)]  # (f = g + h, g, node)
    # Initializing the set of explored nodes
    explored = set()

    # Iterating until the frontier is empty
    while frontier:
        # Pop the node with the minimum f value from the frontier
        _, cost, node = heapq.heappop(frontier)

        # If the node is the destination, return the cost
        if node == dest:
            return cost

        # Add the node to the explored set
        explored.add(node)

        # Iterate over the neighbors of the current node
        for neighbor in adj[node]:
            # If the neighbor has not been explored
            if neighbor.v not in explored:
                # Calculate the new cost
                new_cost = cost + neighbor.weight
                # Calculate the new f value
                f_value = new_cost + heuristic[neighbor.v]
                # Add the neighbor to the frontier with its f value and cost
                heapq.heappush(frontier, (f_value, new_cost, neighbor.v))

    # If no path is found, return infinity
    return float('inf')


""" Making the following graph
'A': {'B':9, 'C':4, 'D':7}
'B': {'A':9, 'E':11}
'C': {'A':4, 'E':17, 'F':12}
'D': {'A':7, 'F':14}
'E': {'B':11, 'C':17, 'Z': 5}
'F': {'C':12, 'D':14, 'Z': 9}
"""

adj = {
    'A': [],
    'B': [],
    'C': [],
    'D': [],
    'E': [],
    'F': [],
    'Z': []
}

addEdge('A', 'B', 9)
addEdge('A', 'C', 4)
addEdge('A', 'D', 7)
addEdge('B', 'A', 9)
addEdge('B', 'E', 11)
addEdge('C', 'A', 4)
addEdge('C', 'E', 17)
addEdge('C', 'F', 12)
addEdge('D', 'A', 7)
addEdge('D', 'F', 14)
addEdge('E', 'B', 11)
addEdge('E', 'C', 17)
addEdge('E', 'Z', 5)
addEdge('F', 'C', 12)
addEdge('F', 'D', 14)
addEdge('F', 'Z', 9)

# Defining the heuristic values for each node.
heuristic = {'A': 21, 'B': 14, 'C': 18, 'D': 18, 'E': 5, 'F': 8, 'Z': 0}

# Finding the shortest path cost using A* Search
cost = AStar('A', 'Z', heuristic)

# Printing the shortest path cost
print("A* Search Cost:", cost)

######################TASK 4 ##################
import heapq

graph = {
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Vaslui': 142, 'Hirsova': 98},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Eforie': {'Hirsova': 86}
}

heuristic_romania = {
    'Arad': 366,
    'Bucharest': 0,
    'Craiova': 160,
    'Drobeta': 242,
    'Eforie': 161,
    'Fagaras': 176,
    'Giurgiu': 77,
    'Hirsova': 151,
    'Iasi': 226,
    'Lugoj': 244,
    'Mehadia': 241,
    'Neamt': 234,
    'Oradea': 380,
    'Pitesti': 100,
    'Rimnicu Vilcea': 193,
    'Sibiu': 253,
    'Timisoara': 329,
    'Urziceni': 80,
    'Vaslui': 199,
    'Zerind': 374
}

# Admissible heuristic: straight-line distance (Euclidean distance) to Bucharest
heuristic_admissible = {
    'Arad': 366,
    'Bucharest': 0,
    'Craiova': 160,
    'Drobeta': 242,
    'Eforie': 161,
    'Fagaras': 176,
    'Giurgiu': 77,
    'Hirsova': 151,
    'Iasi': 226,
    'Lugoj': 244,
    'Mehadia': 241,
    'Neamt': 234,
    'Oradea': 380,
    'Pitesti': 100,
    'Rimnicu Vilcea': 193,
    'Sibiu': 253,
    'Timisoara': 329,
    'Urziceni': 80,
    'Vaslui': 199,
    'Zerind': 374
}


def AStar(graph, heuristic, start, goal):
  
    frontier = [(0 + heuristic[start], 0, start)]  # (f = g + h, g, node)
    explored = set()

    while frontier:
        # Pop the node with the minimum f value from the frontier
        _, cost, node = heapq.heappop(frontier)

        # If the node is the destination, return the cost
        if node == goal:
            return cost

        # Add the node to the explored set
        explored.add(node)

        # Iterate over the neighbors of the current node
        for neighbor, weight in graph[node].items():
            # If the neighbor has not been explored
            if neighbor not in explored:
                # Calculate the new cost
                new_cost = cost + weight
                # Calculate the new f value
                f_value = new_cost + heuristic[neighbor]
                # Add the neighbor to the frontier with its f value and cost
                heapq.heappush(frontier, (f_value, new_cost, neighbor))

    # If no path is found, return infinity
    return float('inf')


start_city = 'Arad'
goal_city = 'Bucharest'

# Finding the shortest path cost using A* Search with the provided heuristic
cost_romania = AStar(graph, heuristic_romania, start_city, goal_city)

# Finding the shortest path cost using A* Search with the admissible heuristic
cost_admissible = AStar(graph, heuristic_admissible, start_city, goal_city)

print("A* Search Cost (Provided Heuristic):", cost_romania)
print("A* Search Cost (Admissible Heuristic):", cost_admissible)



