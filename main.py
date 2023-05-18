import math

from board import *
from robot import Robot
from node import Node

if input("if you enter 1 bot will start the game you will start the game if you enter other numbers :") == '1':
    start_by_user = False
else:
    start_by_user = True

board = Board(start_by_user)
robot = Robot(board)




def select_bead_to_remove(is_user,state):
    if is_user:
        return int(input("please enter an index from bot.beads to remove :"))
    else: return robot.remove_node(state)





game_rond = 1
board.showBoard()
robot.max_depth_search = BOT_LEVEL

while game_rond == 1:
    if board.turn_is_user:
        if board.user_bead_out > 0:
            user_selected = board.add_point(int(input("please select place :")), True,select_bead_to_remove)
            if not user_selected :
                print("invalid input!!!")
            else:
                board.turn_is_user = False
        else :
            board.turn_is_user = False
    else:
        if board.robot_bead_out > 0:
            print("please wait bot is thinking ... 😉")
            node = Node(None,None,board.states,None,(-math.inf,[]),-1)
            robot_selected_node = robot.minimax_rond1(node, True, board.states, board.indexes,board.robot_bead_out,board.user_bead_out)
            print(robot_selected_node.expecti_minimax)
            board.add_point(robot_selected_node.index0, False, select_bead_to_remove)
        board.turn_is_user = True


    print(f"user beads ={board.user_bead_number}      bot beads = {board.robot_bead_number}")
    print(f"user beads out ={board.user_bead_out}      bot beads out = {board.robot_bead_out}")

    if board.beads_ended():
        print("game is done")
        game_rond = 2

robot.board = board

while game_rond == 2:
    if board.turn_is_user:
       indexes = input("please enter 2 numbers to move node (begin destination) :").split(' ')
       if not board.move(True,int(indexes[0]),int(indexes[1]),select_bead_to_remove):
           board.turn_is_user = False
       else : print("please enter begin and destination currectly!!")

    else:
        print("please wait bot is thinking ... 😉")
        node = Node(None, None, board.states, None, (-math.inf, []), -1)
        move = robot.minimax_rond2(node,True,board.states)
        board.move(False,move.index0,move.index1,select_bead_to_remove)
        board.turn_is_user = True







