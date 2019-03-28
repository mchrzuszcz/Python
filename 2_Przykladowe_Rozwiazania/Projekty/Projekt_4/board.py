class Board():

    def __init__(self):
        self.size = 5
        self.board = self.generate_board()
        self.board_ids = self.generate_board_ids()
        self.piece_character = "x"
        self.piece_start_id = "00"
        self.piece_id = self.piece_start_id
        self.set_piece_on_board()

    def generate_board(self):
        board = [["-" for i in range(self.size)] for i in range(self.size)]
        return board

    def generate_board_ids(self):
        board = [["0{}".format(i) for i in range(self.size)]]
        for i in range(10, self.size*10, 10):
            board.append([str(i+j) for j in range(self.size)])
        board.reverse()
        return board

    def set_piece_id(self, place_id):
        self.piece_id = place_id

    def set_piece_on_board(self):
        self.board[(self.size - 1) - int(self.piece_start_id[0])][int(self.piece_start_id[1])] = "-"
        self.board[(self.size-1)-int(self.piece_id[0])][int(self.piece_id[1])] = self.piece_character

    def pretty_print_board(self):
        for i,row in enumerate(self.board):
            print("{} {}".format((self.size-1) - i, " ".join(row)))
        column_ids = [str(i) for i in range(self.size)]
        print("  {}".format(" ".join(column_ids)))