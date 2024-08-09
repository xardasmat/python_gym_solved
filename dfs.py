import unittest

class Graph:
    def __init__(self, graph):
        self.G = graph
        self.visited = set()

    def dfs(self, v):
        self.visited.add(v)
        for n in self.G[v]:
            if not n in self.visited:
                self.dfs(n)

def count_components(graph):

    G = Graph(graph)
    components_count = 0
    for node in graph:
        if not node in G.visited:
            components_count += 1
            G.dfs(node)
    
    return components_count

class TestStringMethods(unittest.TestCase):

    def test_triangle(self):
        #  1 -- 2
        #   \
        #     3
        self.assertEqual(count_components({1: [2, 3], 2: [1], 3: [1]}), 1)

    def test_two_disjoined_paths(self):
        # 1 -- 2
        #
        # 3 -- 4
        self.assertEqual(count_components({1: [2], 2: [1], 3: [4], 4: [3]}), 2)


if __name__ == '__main__':
    unittest.main()
