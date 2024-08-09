import unittest

def count_components(graph):
    #TODO(implement this function pretty please \(^_^)/ )
    # I want it to calculate a number of connected components in the graph.
    # The graph is a list of neighbours. e.g. { 1: [2, 3])}
    return None # this does not work, do it correctly please

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
