import math
import random

from node import Node
from board import *

POINT_COUNT = 24


class Robot:
    def __init__(self, board):
        self.time = None
        self.max_depth_search = 0
        self.board = board

    def minimax_rond1(self, root, is_max, state, reminded_indexes,bot_nodes_num,user_nodes_num):
        if is_max:
            expectiminmax = (-math.inf, self.get_hiuristic_rond1(state, [])[1])
        else:
            expectiminmax = (math.inf, self.get_hiuristic_rond1(state, root.expecti_minimax[1])[1])
        node = Node(root, is_max, state, None, expectiminmax, root.depth + 1)
        if node.depth >= self.max_depth_search or bot_nodes_num<=0 and user_nodes_num <=0:
            node.expecti_minimax = self.get_hiuristic_rond1(state, root.expecti_minimax)
            return node

        if is_max:
            if bot_nodes_num <= 0:
                return self.minimax_rond1(root,False,state,reminded_indexes,bot_nodes_num,user_nodes_num)
            for i in reminded_indexes:
                new_state = state.copy()
                new_state[i] = BOT_CHAR
                not_checked_indexes = reminded_indexes.copy()
                not_checked_indexes.remove(i)
                childe_node = self.minimax_rond1(node, False, new_state, not_checked_indexes,bot_nodes_num-1, user_nodes_num)
                if childe_node.expecti_minimax[0] > node.expecti_minimax[0]:
                    node.expecti_minimax = (childe_node.expecti_minimax[0], node.expecti_minimax[1])
                    node.index0 = i
                    if node.expecti_minimax[0] > node.root.expecti_minimax[0]:
                        return node
        else:
            if user_nodes_num <= 0:
                return self.minimax_rond1(root,True,state,reminded_indexes,bot_nodes_num,user_nodes_num)
            for i in reminded_indexes:
                new_state = state.copy()
                new_state[i] = USER_CHAR
                not_checked_indexes = reminded_indexes.copy()
                not_checked_indexes.remove(i)
                childe_node = self.minimax_rond1(node, True, new_state, not_checked_indexes,bot_nodes_num,user_nodes_num-1)
                if childe_node.expecti_minimax[0] < node.expecti_minimax[0]:
                    node.expecti_minimax = (childe_node.expecti_minimax[0], node.expecti_minimax[1])
                    node.index0 = i
                if node.expecti_minimax[0] < node.root.expecti_minimax[0]:
                    return node
        return node

    def get_hiuristic_rond1(self, state, previous_wins):
        hiuristic = 0
        current_wins = []
        for item in WIN_STATES:
            if item not in previous_wins and state[item[0]] == BOT_CHAR and state[item[1]] == BOT_CHAR and state[
                item[2]] == BOT_CHAR:
                hiuristic += 1
                current_wins.append(item)
            elif item not in previous_wins and state[item[0]] == USER_CHAR and state[item[1]] == USER_CHAR and state[
                item[2]] == USER_CHAR:
                hiuristic -= 1
                current_wins.append(item)
        return (hiuristic, current_wins)



    def minimax_rond2(self, root, is_max, state):
        if is_max:
            expectiminmax = (-math.inf, self.get_hiuristic_rond1(state, [])[1])
        else:
            expectiminmax = (math.inf, self.get_hiuristic_rond1(state, [])[1])

        node = Node(root, is_max, state, None, expectiminmax, root.depth + 1)

        if node.depth >= self.max_depth_search*1.5 or self.board.user_bead_number == 3 or self.board.robot_bead_number == 3:
            node.expecti_minimax = (self.get_hiuristic_rond2(state),[])
            return node

        if is_max:
            for i in range(0, len(state)):
                if state[i] == BOT_CHAR:
                    node.index0 = i
                    for j in MOVEMENT_STATES[i]:
                        if state[j] == ' ':
                            node.index1 = j
                            new_state_for_move = state.copy()
                            new_state_for_move[j] = new_state_for_move[i]  # move bead
                            new_state_for_move[i] = ' '
                            h_after_movement = self.get_hiuristic_rond1(new_state_for_move, node.expecti_minimax[1])
                            if h_after_movement[0] > 0:
                                for k in range(0, len(new_state_for_move)):
                                    new_state_for_remove = new_state_for_move.copy()
                                    if new_state_for_remove[k] == USER_CHAR:
                                        new_state_for_remove[k] = ' '
                                        childe_node = self.minimax_rond2(node, False, new_state_for_remove)
                                        if childe_node.expecti_minimax[0] > node.expecti_minimax[0]:
                                            node.expecti_minimax = (childe_node.expecti_minimax[0], node.expecti_minimax[1])
                                            node.index0 = i
                                            node.index1 = j
                                        if node.expecti_minimax[0] > root.expecti_minimax[0]:
                                            return node
                            else:
                                childe_node = self.minimax_rond2(node, False, new_state_for_move)
                                if childe_node.expecti_minimax[0] > node.expecti_minimax[0]:
                                    node.expecti_minimax = (childe_node.expecti_minimax[0], node.expecti_minimax[1])
                                    node.index0 = i
                                    node.index1 = j
                                if node.expecti_minimax[0] > root.expecti_minimax[0]:
                                    return node
            return node


        else:
            for i in range(0, len(state)):
                if state[i] == USER_CHAR:
                    node.index0 = i
                    for j in MOVEMENT_STATES[i]:
                        if state[j] == ' ':
                            node.index1 = j
                            new_state_for_move = state.copy()
                            new_state_for_move[j] = new_state_for_move[i]  # move bead
                            new_state_for_move[i] = ' '
                            h_after_movement = self.get_hiuristic_rond1(new_state_for_move, node.expecti_minimax[1])
                            if h_after_movement[0] < 0:
                                for k in range(0, len(new_state_for_move)):
                                    new_state_for_remove = new_state_for_move.copy()
                                    if new_state_for_remove[k] == BOT_CHAR:
                                        new_state_for_remove[k] = ' '
                                        childe_node = self.minimax_rond2(node, False, new_state_for_remove)
                                        if childe_node.expecti_minimax[0] < node.expecti_minimax[0]:
                                            node.expecti_minimax = (childe_node.expecti_minimax[0], node.expecti_minimax[1])
                                            node.index0 = i
                                            node.index1 = j
                                        if node.expecti_minimax[0] < root.expecti_minimax[0]:
                                            return node
                            else:
                                childe_node = self.minimax_rond2(node, False, new_state_for_move)
                                if childe_node.expecti_minimax[0] > node.expecti_minimax[0]:
                                    node.expecti_minimax = (childe_node.expecti_minimax[0], node.expecti_minimax[1])
                                    node.index0 = i
                                    node.index1 = j
                                if node.expecti_minimax[0] > root.expecti_minimax[0]:
                                    return node
            return node

    def remove_node(self, state):
        user_nodes = []
        for i in range(0, len(state)):
            if state[i] == USER_CHAR:
                user_nodes.append(i)
        return random.randint(0, len(user_nodes))

    def get_hiuristic_rond2(self, state):
        bot_beads_number = 0
        user_beads_number = 0
        for item in state:
            if item == BOT_CHAR:
                bot_beads_number += 1
            elif item == USER_CHAR:
                user_beads_number += 1

        return bot_beads_number - user_beads_number
