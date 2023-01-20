import math


class Node:
    def __init__(self, root, is_max, state, index, depth):
        self.root = root
        self.is_max = is_max
        self.state = state
        self.index = index
        self.depth = depth
        if is_max:
            self.expecti_minimax = -math.inf
        else:
            self.expecti_minimax = math.inf
