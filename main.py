from board import Board
from robot import Robot
from node import Node

board = Board()
robot = Robot()

game_is_on = True
game_rond = 1
if input("if you enter 1 bot will start the game you will start the game if you enter other numbers :") == '1':
    start_by_user = False
else:
    start_by_user = True

board.showBoard()
while game_is_on:
    if start_by_user:
        user_selected = board.add_point(input("please select place :"), True)
        if user_selected == None:
            print("invalid input!!!")
        else:
            print("please wait bot is thinking ... 😊")
            node = Node(None, None, None, None, -1)
            robot.max_depth_search = game_rond + 5
            robot_selected_node = robot.minimax(node, True, board.state, board.indexes)
            print(robot_selected_node.expecti_minimax)
            board.add_point(robot_selected_node.index, False)
    else:
        print("please wait bot is thinking ... 😊")
        node = Node(None, None, None, None, -1)
        robot.max_depth_search = game_rond + 4
        robot_selected_node = robot.minimax(node, True, board.state, board.indexes)
        print(robot_selected_node.expecti_minimax)
        board.add_point(robot_selected_node.index, False)
        user_selected = board.add_point(input("please select place :"), True)
        if user_selected == None:
            print("invalid input!!!")

    if board.board_is_full():
        print("game is done")
        game_is_on = False
