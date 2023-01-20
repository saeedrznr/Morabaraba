from node import Node
from board import *

POINT_COUNT = 24


class Robot:
    def __init__(self):
        self.time = None
        self.max_depth_search = 0

    def minimax(self, root, is_max, state, reminded_indexes):

        node = Node(root, is_max, state, None, root.depth + 1)
        if node.depth >= self.max_depth_search or len(reminded_indexes) == 0:
            node.expecti_minimax = self.calculate_expectiminimax(state)
            return node

        if is_max:
            for i in reminded_indexes:
                new_state = state.copy()
                new_state[i] = BOT_CHAR
                not_checked_indexes = reminded_indexes.copy()
                not_checked_indexes.remove(i)
                childe_node = self.minimax(node, False, new_state, not_checked_indexes)
                if childe_node.expecti_minimax > node.expecti_minimax:
                    node.expecti_minimax = childe_node.expecti_minimax
                    node.index = i
                    if node.expecti_minimax > node.root.expecti_minimax:
                        return node
        else:
            for i in reminded_indexes:
                new_state = state.copy()
                new_state[i] = USER_CHAR
                not_checked_indexes = reminded_indexes.copy()
                not_checked_indexes.remove(i)
                childe_node = self.minimax(node, True, new_state, not_checked_indexes)
                if childe_node.expecti_minimax < node.expecti_minimax:
                    node.expecti_minimax = childe_node.expecti_minimax
                    node.index = i
                if node.expecti_minimax < node.root.expecti_minimax:
                    return node
        return node

    def calculate_expectiminimax(self, state):
        expectiminimax = 0

        for item in WIN_STATES:
            if state[item[0]] == BOT_CHAR and state[item[1]] == BOT_CHAR and state[item[2]] == BOT_CHAR:
                expectiminimax += 1
            elif state[item[0]] == USER_CHAR and state[item[1]] == USER_CHAR and state[item[2]] == USER_CHAR:
                expectiminimax -= 1
        return expectiminimax
