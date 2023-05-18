class Node:
    def __init__(self, root, is_max, state, index, expectiminimax, depth):
        self.root = root
        self.is_max = is_max
        self.state = state
        self.index0 = index
        self.index1 = 0
        self.depth = depth
        self.expecti_minimax = expectiminimax


