BOT_CHAR = '#'
USER_CHAR = '&'
WIN_STATES = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11), (12, 13, 14), (15, 16, 17), (18, 19, 20), (21, 22, 23),
              # horizontal
              (0, 9, 21), (3, 10, 18), (6, 11, 15), (1, 4, 7), (16, 19, 22), (8, 12, 17), (5, 13, 20), (2, 14, 23),
              # vertical
              (0, 3, 6), (2, 5, 8), (17, 20, 23), (15, 18, 21)
              # diagonal
              ]

TOTAL_INDEXES = [0, 5, 15, 8, 18, 2, 3, 17, 23, 6, 21, 20, 1, 10, 12, 11, 14, 16, 4, 9, 13, 22, 7, 19]

BOT_LEVEL = 4


class Board:
    def __init__(self):
        self.robot_grade = 0
        self.user_grade = 0
        self.robot_bead_number = 12
        self.user_bead_number = 12
        self.robot_bead_out = 12
        self.user_bead_out = 12

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
        if is_user:
            grade_before_adding = self.calculate_grade()
            self.states[index] = self.states[index] = USER_CHAR
            grade_after_adding = self.calculate_grade()
            self.user_bead_out -= 1
            if grade_before_adding > grade_after_adding:  # user sets 3 in line
                if self.robot_bead_out > 0:
                    self.robot_bead_out -= 1
                    self.robot_bead_number -= 1
                else:
                    will_be_removed_index = call_back(True)
                    self.states[will_be_removed_index] = ' '
                    self.indexes.append(TOTAL_INDEXES[will_be_removed_index])
            print(self.indexes)
            self.indexes.remove(index)


        else:
            grade_before_adding = self.calculate_grade()
            self.states[index] = self.states[index] = BOT_CHAR
            grade_after_adding = self.calculate_grade()
            self.robot_bead_out -= 1
            if grade_after_adding > grade_before_adding:  # bot sets 3 in line
                if self.user_bead_out > 0:
                    self.user_bead_out -= 1
                    self.user_bead_number -= 1
                else:
                    will_be_removed_index = call_back(False)
                    self.states[will_be_removed_index] = ' '
                    self.indexes.append(TOTAL_INDEXES[will_be_removed_index])
            self.indexes.remove(index)

        self.robot_grade = self.calculate_grade()
        self.user_grade = -1 * self.robot_grade

        self.showBoard()

        return index

    def beads_ended(self):
        if self.user_bead_out == 0 and self.robot_bead_out == 0:
            return True
        return False

    def calculate_grade(self):
        grade = 0
        for item in WIN_STATES:
            if self.states[item[0]] == BOT_CHAR and self.states[item[1]] == BOT_CHAR and self.states[
                item[2]] == BOT_CHAR:
                grade += 1
            elif self.states[item[0]] == USER_CHAR and self.states[item[1]] == USER_CHAR and self.states[
                item[2]] == USER_CHAR:
                grade -= 1
        return grade
