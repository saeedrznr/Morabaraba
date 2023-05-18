BOT_CHAR = '#'
USER_CHAR = '&'
WIN_STATES = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11), (12, 13, 14), (15, 16, 17), (18, 19, 20), (21, 22, 23),
              # horizontal
              (0, 9, 21), (3, 10, 18), (6, 11, 15), (1, 4, 7), (16, 19, 22), (8, 12, 17), (5, 13, 20), (2, 14, 23),
              # vertical
              (0, 3, 6), (2, 5, 8), (17, 20, 23), (15, 18, 21)
              # diagonal
              ]

MOVEMENT_STATES = [[9, 3, 1], [0, 4, 2], [1, 5, 14],
                   [0, 10, 4, 6], [3, 1, 5, 7], [4, 2, 8, 13],
                   [11, 3, 7], [6, 4, 8], [7, 5, 12],
                   [0, 21, 10], [9, 3, 18, 11], [10, 15, 6],
                   [8, 17, 13], [12, 5, 20, 14], [13, 2, 23],
                   [11, 18, 16], [15, 19, 17], [16, 12, 20],
                   [10, 21, 19, 15], [18, 16, 22, 20], [19, 17, 23, 13],
                   [9, 18, 22], [21, 19, 23], [22, 20, 14]]

TOTAL_INDEXES = [0, 5, 15, 8, 18, 2, 3, 17, 23, 6, 21, 20, 1, 10, 12, 11, 14, 16, 4, 9, 13, 22, 7, 19]

BOT_LEVEL = 5


class Board:
    def __init__(self, turn_is_user):
        self.robot_grade = 0
        self.user_grade = 0
        self.robot_bead_number = 12
        self.user_bead_number = 12
        self.robot_bead_out = 12
        self.user_bead_out = 12
        self.turn_is_user = turn_is_user
        self.wins = []

        self.indexes = [0, 5, 15, 8, 18, 2, 3, 17, 23, 6, 21, 20, 1, 10, 12, 11, 14, 16, 4, 9, 13, 22, 7, 19]

        self.states = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
            , ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def showBoard(self):
        if self.user_grade > 0:
            grade = f"0:{self.user_grade}"
        elif self.robot_grade > 0:
            grade = f"{self.robot_grade}:0"
        else:
            grade = "0:0"
        print(f"""
                    {self.states[0]}-------------{self.states[1]}-------------{self.states[2]}
                    |  .          |          .  |                                          
                    |    {self.states[3]}--------{self.states[4]}--------{self.states[5]}    |
                    |    |  .     |      . |    |                               
                    |    |   {self.states[6]}----{self.states[7]}----{self.states[8]}   |    |
                    |    |   |         |   |    |
                    {self.states[9]}----{self.states[10]}---{self.states[11]}   {grade}   {self.states[12]}---{self.states[13]}----{self.states[14]}
                    |    |   |         |   |    |                                          
                    |    |   {self.states[15]}----{self.states[16]}----{self.states[17]}   |    |
                    |    | .      |      . |    |                                          
                    |    {self.states[18]}--------{self.states[19]}--------{self.states[20]}    |
                    |  .          |           . |
                    {self.states[21]}-------------{self.states[22]}-------------{self.states[23]}
                    """)

    def add_point(self, index, is_user: bool, call_back):
        grade_before_adding = self.robot_grade
        if is_user:
            if index in self.indexes:
                self.states[index] = self.states[index] = USER_CHAR
                self.user_bead_out -= 1
                print(self.indexes)
                self.indexes.remove(index)
                return True
            else:
                return False
        else:
            self.states[index] = self.states[index] = BOT_CHAR
            self.robot_bead_out -= 1
            self.indexes.remove(index)

        self.calculate_grade()


        self.showBoard()

        grade_after_adding = self.robot_grade

        if grade_before_adding > grade_after_adding:  # user sets 3 in same line
            if self.robot_bead_out > 0:
                self.robot_bead_out -= 1
                self.robot_bead_number -= 1
            else:
                will_be_removed_index = call_back(True, self.states)
                self.update_toatal_win_state()
                self.states[will_be_removed_index] = ' '
                self.indexes.append(TOTAL_INDEXES[will_be_removed_index])
        elif grade_before_adding < grade_after_adding:  # bot sets 3 in same line
            if self.user_bead_out > 0:
                self.user_bead_out -= 1
                self.user_bead_number -= 1
            else:
                will_be_removed_index = call_back(False, self.states)
                self.update_toatal_win_state()
                self.states[will_be_removed_index] = ' '
                self.indexes.append(TOTAL_INDEXES[will_be_removed_index])

        self.showBoard()

        return index

    def move(self, is_user, begin, des,call_back):
        grade_bofore_move = self.robot_grade
        if is_user:
            if self.states[begin] == USER_CHAR and self.states[des] == ' ':
                self.states[des] = USER_CHAR
                self.states[begin] = ' '
            else:
                return False
        else:
            self.states[des] = BOT_CHAR
            self.states[begin] = ' '

        self.showBoard()
        self.calculate_grade()
        grade_after_move = self.robot_grade
        if grade_bofore_move > grade_after_move:  # user sets 3 in same line
                will_be_removed_index = call_back(True, self.states)
                self.update_toatal_win_state()
                self.update_toatal_win_state()
                self.states[will_be_removed_index] = ' '
                self.indexes.append(TOTAL_INDEXES[will_be_removed_index])
        elif grade_bofore_move < grade_after_move:  # bot sets 3 in same line
                will_be_removed_index = call_back(False, self.states)
                self.update_toatal_win_state()
                self.update_toatal_win_state()
                self.states[will_be_removed_index] = ' '
                self.indexes.append(TOTAL_INDEXES[will_be_removed_index])


    def beads_ended(self):
        if self.user_bead_out == 0 and self.robot_bead_out == 0:
            return True
        return False

    def calculate_grade(self):
        for item in WIN_STATES:
            if self.states[item[0]] == BOT_CHAR and self.states[item[1]] == BOT_CHAR and self.states[
                item[2]] == BOT_CHAR and item not in self.wins:
                self.robot_grade += 1
                self.user_grade -= 1
                self.wins.append(item)
            elif self.states[item[0]] == USER_CHAR and self.states[item[1]] == USER_CHAR and self.states[
                item[2]] == USER_CHAR and item not in self.wins:
                self.user_grade += 1
                self.robot_grade -= 1
                self.wins.append(item)


    def update_toatal_win_state(self):
        self.wins = []
        for item in WIN_STATES:
            if self.states[item[0]] == BOT_CHAR and self.states[item[1]] == BOT_CHAR and self.states[
                item[2]] == BOT_CHAR:
                self.wins.append(item)
            elif self.states[item[0]] == USER_CHAR and self.states[item[1]] == USER_CHAR and self.states[
                item[2]] == USER_CHAR :
                self.wins.append(item)

