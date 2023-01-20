from board import *
from robot import Robot
from node import Node

board = Board()
robot = Robot()




def select_bead_to_remove(is_user):
    return int(input("please enter an index from bot.beads to remove :"))


if input("if you enter 1 bot will start the game you will start the game if you enter other numbers :") == '1':
    start_by_user = False
else:
    start_by_user = True

game_rond = 1
board.showBoard()
while game_rond == 1:
    if start_by_user:
        if board.user_bead_out > 0:
            user_selected = board.add_point(int(input("please select place :")), True,select_bead_to_remove)
            if user_selected == None:
                print("invalid input!!!")
            else:
                if board.robot_bead_number > 0:
                    print("please wait bot is thinking ... 😊")
                    node = Node(None, None, None, None,-1)
                    robot.max_depth_search = BOT_LEVEL
                    robot_selected_node = robot.minimax(node, True, board.states, board.indexes)
                    print(robot_selected_node.expecti_minimax)
                    board.add_point(robot_selected_node.index, False,select_bead_to_remove)
    else:
        if board.robot_bead_out > 0:
            print("please wait bot is thinking ... 😉")
            node = Node(None,None,board.states,None,-1)
            robot.max_depth_search = BOT_LEVEL
            robot_selected_node = robot.minimax(node, True, board.states, board.indexes)
            print(robot_selected_node.expecti_minimax)
            board.add_point(robot_selected_node.index, False,select_bead_to_remove)
            if board.user_bead_number > 0 :
                user_selected = board.add_point(int(input("please select place :")), True,select_bead_to_remove)
                if user_selected == None:
                    print("invalid input!!!")

    print(f"user beads ={board.user_bead_number}      bot beads = {board.robot_bead_number}")
    print(f"user beads out ={board.user_bead_out}      bot beads out = {board.robot_bead_out}")

    if board.beads_ended():
        print("game is done")
        game_rond = 2


