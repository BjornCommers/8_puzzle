from queue import Queue
from collections import defaultdict

class Graph:

    def __init__(self, V, E):
        self.vertices = {}
        for v in V:
            self.vertices[v] = []
        for x, y in E:
            if y not in self.vertices[x]:
                self.vertices[x].append(y)
            if x not in self.vertices[y]:
                self.vertices[y].append(x)

    def neighbors(self, u):
        return self.vertices[u]

    def dist_between(self, u, v):
        if v in self.vertices[u]:
            return 1
        else:
            return None


def BFS(G, start, goal):
    frontier = Queue()
    discovered = defaultdict(lambda: False)
    parent = {}

    # TODO: implement
    frontier.put(start)
    discovered[start] = True

    while frontier:
        v = frontier.get()
        if v == goal:
            break
        for w in G.neighbors(v):
            if discovered[w] is False:
                discovered[w] = True
                parent[w] = v
                frontier.put(w)
    return reconstruct_path(start, goal, parent)


def DFS_recursive(G, start, goal):
    discovered = defaultdict(lambda: False)
    parent = {}

    # TODO: implement



    return reconstruct_path(start, goal, parent)

def DFS_recursive_helper(G, current, goal):

def DFS_iterative(G, start, goal):
    discovered = defaultdict(lambda: False)
    parent = {}
    stack = []

    # TODO: implement
    stack.append(start)
    while stack:
        v = stack.pop()
        if v == goal:
            break
        if discovered[v] is False:
            discovered[v] = True
            for w in G.neighbors(v):
                stack.append(w)
                if discovered[w] is False:
                    parent[w] = v
    return reconstruct_path(start, goal, parent)


def reconstruct_path(start, goal, parent):
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = parent[current]
    return path

