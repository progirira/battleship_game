class Move(object):
    def __init__(self, row, column):
        self.row = int(row)
        self.column = int(column)

        self.rotation = None
        self.number_of_decks = 1
        self.if_correct = True

    def check_errors(self, x_move, y_move):
        x_move = abs(x_move)
        y_move = abs(y_move)
        if x_move * y_move != 0 or x_move > 1 or y_move > 1:
            self.if_correct = False
        if (self.rotation == 'v' and y_move > 0) or (self.rotation == 'h'
                                                     and x_move > 0):
            self.if_correct = False

        if x_move == 0 and y_move == 0:
            self.if_correct = False

    def add_info(self, x, y):

        x_move = x - self.row
        y_move = y - self.column
        if self.rotation == 'h' and abs(y - (self.column + self.number_of_decks
                                          - 1)) == 1:
            y_move = y - (self.column + self.number_of_decks - 1)
        elif self.rotation == 'v' and abs(x - (self.row +
                                               self.number_of_decks - 1)) == 1:
            x_move = x - (self.row + self.number_of_decks - 1)

        self.check_errors(x_move, y_move)

        if self.if_correct:
            self.add_coor(x_move, y_move)

    def add_coor(self, x, y):
        if self.rotation is None:
            if x != 0:
                self.rotation = 'v'
            else:
                self.rotation = 'h'
        if x == -1 or y == -1:
            self.row += x
            self.column += y
        self.number_of_decks += 1

