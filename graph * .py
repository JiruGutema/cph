from collections import defaultdict
from collections import deque

n = 10  
A = [
    [0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 0],
    [0, 2], [2, 4], [4, 6], [6, 8], [8, 0],  
    [1, 1], [3, 3], [5, 5], 
    [2, 5], [5, 2], [7, 9], [9, 7]  
]

class Graph:
    def __init__(self):
        self.D = defaultdict()
        self.seen = set()
        self.stack = [0]
        self.queue = deque()


    def print_matrix(self, matrix):
        if isinstance(matrix, dict): 
            for key, value in matrix.items():
                print(f"{key}: {value}")
        else:  
            for row in matrix:
                print(row)

    def adjacency_matrix_directed(self, n, A):
        matrix = [[0]*n for _ in range(n)]
        for v, u in A:
            matrix[v][u] = 1 
        print("Directed graph")
        self.print_matrix(matrix)

    def adjacency_matrix_undirected(self, n, A):
        matrix = [[0]*n for _ in range(n)]
        for u, v in A:
            matrix[u][v] = 1
            matrix[v][u] = 1 
        print("Undirected graph")
        self.print_matrix(matrix)

    def adjacency_list_directed(self, n, A):
        connected = defaultdict(list)
        for u, v in A:
            connected[u].append(v)
            self.D[u] = v
        print("Directed adjacency list")
        self.print_matrix(connected)

    def adjacency_list_undirected(self, n, A):
        connected = defaultdict(list)
        for u, v in A:
            connected[u].append(v)
            connected[v].append(u)
        print("Undirected adjacency list")
        self.print_matrix(connected)

    def dfs_recursion(self, node):
        # process the current node
        print(node)
        for nie_bor in self.D[node]:
            if nie_bor not in self.seen:
                self.seen.add(nie_bor)
                self.dfs_recursion(nie_bor)
    
    def dfs_iterative(self, start_node):
        self.stack = [start_node]
        self.seen = set([start_node])  # mark start node as seen

        while self.stack:
            node = self.stack.pop()
            print(node)  # process current node
            for neighbor in self.D[node]:
                if neighbor not in self.seen:
                    self.seen.add(neighbor)
                    self.stack.append(neighbor)
    def bfs_iterative(self, node):
        pass


        
    

        
        


graph = Graph()
# graph.adjacency_list_undirected(n, A)
graph.adjacency_list_directed(n, A)
# graph.adjacency_matrix_directed(n, A)
# graph.adjacency_matrix_undirected(n, A)
print("dfs")
graph.dfs_recursion(0)
print("bfs")
graph.dfs_iterative(0)