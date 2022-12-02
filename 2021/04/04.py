with open("boards.txt") as f:
    data = f.readlines()

input_nums = data[0].split(",")


class BingoBoard:
    def __init__(self, board_list):
        self.board = [
            BingoBoard._get_row(board_list[0]),
            BingoBoard._get_row(board_list[1]),
            BingoBoard._get_row(board_list[2]),
            BingoBoard._get_row(board_list[3]),
            BingoBoard._get_row(board_list[4]),
        ]
        self.print_board()
        self.found_nums = []

        self.called = [[0] * 5, [0] * 5, [0] * 5, [0] * 5, [0] * 5]

    @staticmethod
    def _get_row(s):
        arr = []
        for x in s.split(" "):
            if x != "":
                arr.append(x)
        if arr[-1][-1] == "\n":
            arr[-1] = arr[-1][:-1]
        return arr

    def print_board(self):
        print("BOARD")
        for row in self.board:
            print(row)

    def print_called(self):
        print("CALLED")
        for row in self.called:
            print(row)

    def calc_score(self):
        if not self.did_win():
            return -1

        score = 0
        for row in range(len(self.board)):
            for col in range(len(self.board)):
                if self.called[row][col] == 0:
                    score += int(self.board[row][col])
        return score

    def call_num(self, num):
        if self.did_win():
            return
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] == num:
                    self.found_nums.append(num)
                    # print(f"FOUND NUMBER AT {row}, {col}")
                    self.called[row][col] = 1
                    if self.did_win():
                        print("WON WON WON WON")

                        self.print_board()
                        self.print_called()
                        print(f"Nums found: {self.found_nums}")

                        print("")
                        print(f"SCORE = {self.calc_score()} after called {num}")
                        answer = self.calc_score() * int(num)
                        print(f"ANSWER = {self.calc_score() * int(num)}")
                        print("")

    def did_win(self):
        for row in self.called:
            if sum(row) == len(row):
                return True
        for col in range(len(self.called) - 1):
            total = 0
            for row in self.called:
                total += row[col]
            if total == len(self.called):
                return True
        return False


boards = []
for row in range(2, len(data), 6):
    board = BingoBoard(data[row : row + 5])
    boards.append(board)

print(f"boards loaded: {len(boards)}")


# input_nums = ['1','67','4','58','13']
winners = []
for input_num in input_nums:
    print(f"Calling number {input_num}")
    # i = 1
    # boards[i].call_num(input_num)
    # boards[i].print_board()
    # boards[i].print_called()
    for board in boards:
        board.call_num(input_num)
        # if board.did_win():
        #     print("Found a winner")
        #     winners.append(board)


# winner = winners[-1]
# winner.print_board()

# winner.print_called()
# print(f"Nums found: {winner.found_nums}")

# print("")
# print(f"SCORE = {winner.calc_score()} after called {winner.found_nums[-1]}")
# print(f"ANSWER = {winner.calc_score() * winner.found_nums[-1]}")
# print("")


# print("NOT 624")
