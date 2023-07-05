class TicTacToe:
    place_history = []
    row_max = 3
    col_max = 3
    prev_player = "O"
    place_n = "X"
    win = ""

    def __init__(self):
        self.table = self.form_table()

    def form_table(self, v=" "):
        table = []
        for x in range(self.row_max):
            temp_l = []
            for y in range(self.col_max):
                temp_l.append(v)
            table.append(temp_l)
        return table

    def win_rule(self):
        # 123, 456, 789, 147, 258, 369, 159, 357
        # horizontal
        for x in range(self.row_max):
            v = "".join(self.table[x])
            if v.count(self.place_n) == self.row_max:
                self.win = self.place_n
                return True

        # vertical
        for x in range(self.row_max):
            v = ""
            for y in range(self.col_max):
                v += self.table[y][x]
            if v.count(self.place_n) == self.row_max:
                self.win = self.place_n
                return True

        # left
        v = ""
        for x in range(self.row_max):
            for y in range(self.col_max):
                if x == y:
                    v += self.table[x][y]
        if v.count(self.place_n) == self.row_max:
            self.win = self.place_n
            return True

        # right
        v = ""
        for x in range(self.row_max):
            for y in range(self.col_max):
                if x == self.col_max - y - 1:
                    v += self.table[x][y]
        if v.count(self.place_n) == self.row_max:
            self.win = self.place_n
            return True
        return False

    def predict_win(self, player=None):
        # 12 or 23, 45 or 56, 78 or 89, 14 or 47, 25 or 58, 36 or 69, 15 or 59, 35 or 57
        if player is None:
            player = self.prev_player

        for x in range(self.row_max):
            v = ""
            empty = -1
            for y in range(self.col_max):
                v += self.table[x][y]
                if self.table[x][y] == " ":
                    empty = y
            if v.count(player) == self.row_max - 1 and (empty != -1 or player == self.place_n):
                return [x, empty]

        # vertical
        for x in range(self.row_max):
            v = ""
            empty = -1
            for y in range(self.col_max):
                v += self.table[y][x]
                if self.table[y][x] == " ":
                    empty = y
            if v.count(player) == self.row_max - 1 and (empty != -1 or player == self.place_n):
                return [empty, x]

        return [2, 2]

    def print_table(self):
        print("Player %s" % self.place_n)
        total_len = len("".join(self.table[0])) + len(self.table[0]) + 2 * len(self.table[0])
        for count2, r in enumerate(self.table):
            for count, x in enumerate(r):
                if count < len(r) - 1:
                    print(" " + x + " ", end="|")
                else:
                    print(" " + x + " ")
                    if count2 != len(self.table) - 1:
                        print("-" * total_len)
        print()

    def check(self, row, col):
        if row >= self.row_max:
            print("row must no more than %s " % self.row_max)
            return False
        if col >= self.col_max:
            print("row must no more than %s " % self.col_max)
            return False
        for x in self.place_history:
            if [row, col] == x:
                print("Try put other place")
                return False
        return True

    def switch_player(self):
        if self.place_n == "X":
            self.prev_player = "X"
            self.place_n = "O"
        else:
            self.prev_player = "O"
            self.place_n = "X"

    def place_f(self, row=None, col=None):
        if row is None and row is None:
            return False
        if self.check(row, col):
            self.table[row][col] = "%s" % self.place_n
            self.place_history.append([row, col])
            if self.win_rule():
                print("Winner is %s" % self.place_n)
                return True
            self.switch_player()
            return True
        return False

    def pvp(self):
        for x in range(self.row_max * self.col_max):
            if self.win:
                break
            row, col = None, None
            while not self.place_f(row, col):
                if len(self.place_history) == (self.col_max * self.row_max) or self.win:
                    break
                row = int(input("select row: "))
                col = int(input("select col: "))
            self.print_table()

    def calc(self):
        len_h = len(self.place_history)
        if len_h == 1:
            if self.table[1][1] != self.prev_player:
                self.place_f(1, 1)
            else:
                choice_list = [[0, 0], [0, 2], [2, 0], [2, 2]]
                for x in choice_list:
                    if self.place_f(x[0], x[1]):
                        break
        else:
            row, col = None, None
            count = 0
            if len_h == 3:
                while not self.place_f(row, col):
                    if count == 0:
                        [row, col] = self.predict_win()
                        count += 1
                    else:
                        [row, col] = self.predict_win(self.place_n)
            else:
                while not self.place_f(row, col):
                    if count == 0:
                        [row, col] = self.predict_win(self.place_n)
                        count += 1
                    else:
                        [row, col] = self.predict_win()

    def pvc(self):
        pass

    def play(self):
        command = 0
        while command != 3:
            if self.win:  # for reset purpose
                print("Play Again?")
                self.win = ""
            print("1 - Player vs Player \n")
            # print("2 - Player vs Computer \n")
            print("3 - Quit? \n")
            command = int(input("Please Select: "))
            if command == 1:
                self.pvp()
            elif command == 2:
                self.pvc()


# start
c = TicTacToe()
c.play()
