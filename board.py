BOT_CHAR = '#'
USER_CHAR = '&'
WIN_STATES = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11), (12, 13, 14), (15, 16, 17), (18, 19, 20), (21, 22, 23),
              # horizontal
              (0, 9, 21), (3, 10, 18), (6, 11, 15), (1, 4, 7), (16, 19, 22), (8, 12, 17), (5, 13, 20), (2, 14, 23),
              # vertical
              (0, 3, 6), (2, 5, 8), (17, 20, 23), (15, 18, 21)
              # diagonal
              ]


class Board:
    def __init__(self):
        self.robot_grade = 0
        self.user_grade = 0

        self.indexes = [0, 5, 15, 8, 18, 2, 3, 17, 23, 6, 21, 20, 1, 10, 12, 11, 14, 16, 4, 9, 13, 22, 7, 19]
        # self.indexes = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
        self.points = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c'
            , 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']

        self.state = ['', '', '', '', '', '', '', '', '', '', ''
            , '', '', '', '', '', '', '', '', '', '', '', '', '']

    def showBoard(self):
        if self.user_grade > 0:
            grade = f"0:{self.user_grade}"
        elif self.robot_grade > 0:
            grade = f"{self.robot_grade}:0"
        else:
            grade = "0:0"
        print(f"""
                    {self.points[0]}-------------{self.points[1]}-------------{self.points[2]}
                    |  .          |          .  |                                          
                    |    {self.points[3]}--------{self.points[4]}--------{self.points[5]}    |
                    |    |  .     |      . |    |                               
                    |    |   {self.points[6]}----{self.points[7]}----{self.points[8]}   |    |
                    |    |   |         |   |    |
                    {self.points[9]}----{self.points[10]}---{self.points[11]}   {grade}   {self.points[12]}---{self.points[13]}----{self.points[14]}
                    |    |   |         |   |    |                                          
                    |    |   {self.points[15]}----{self.points[16]}----{self.points[17]}   |    |
                    |    | .      |      . |    |                                          
                    |    {self.points[18]}--------{self.points[19]}--------{self.points[20]}    |
                    |  .          |           . |
                    {self.points[21]}-------------{self.points[22]}-------------{self.points[23]}
                    """)

    def add_point(self, n, is_user: bool):
        index = None
        if is_user:
            for i in range(0, len(self.points)):
                if self.points[i] == n.lower():
                    index = i
                    break
            if index == None: return index
            self.state[index] = self.points[index] = USER_CHAR
            self.indexes.remove(index)

        else:
            if n not in self.indexes: return False
            self.state[n] = self.points[n] = BOT_CHAR
            self.indexes.remove(n)

        self.robot_grade = self.calculate_grade()
        self.user_grade = -1 * self.robot_grade

        self.showBoard()

        return index

    def board_is_full(self):
        return len(self.indexes) == 0

    def calculate_grade(self):
        grade = 0
        for item in WIN_STATES:
            if self.state[item[0]] == BOT_CHAR and self.state[item[1]] == BOT_CHAR and self.state[item[2]] == BOT_CHAR:
                grade += 1
            elif self.state[item[0]] == USER_CHAR and self.state[item[1]] == USER_CHAR and self.state[
                item[2]] == USER_CHAR:
                grade -= 1
        return grade
