import math
import robot


class Node:
    def __init__(self, root, is_max, state, index, depth):
        self.root = root
        self.is_max = is_max
        self.state = state
        self.index = index
        self.depth = depth
        bot = robot.Robot()
        if is_max == None:
           self.expecti_minimax = (math.inf, bot.get_hiuristic(state,[])[1])
        else:
            if is_max:
                self.expecti_minimax = (-math.inf, bot.get_hiuristic(state, [])[1])
            else:
                self.expecti_minimax = (math.inf, bot.get_hiuristic(state, [])[1])
