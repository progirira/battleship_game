from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QGridLayout, QLayout

from model.move import Move
from model.position import Position
from model.shipfactory import ShipFactory


class Field:

    def __init__(self, dim):
        self.move = None
        self.positions = QGridLayout()
        self.positions.setSpacing(5)

        self.positions.setSizeConstraint(QLayout.SetFixedSize)
        self.dim = dim
        self.init_board()
        # self.wrong_move = True
        # self.ships_factory = ShipFactory()
        # self.ships_factory = None

    def init_board(self):
        # Add positions to the map
        for x in range(0, self.dim):
            for y in range(0, self.dim):
                w = Position(x, y)
                self.positions.addWidget(w, y, x)
                w.clicked.connect(self.if_clicked)

    def if_clicked(self):
        for x in range(0, self.dim):
            for y in range(0, self.dim):
                w = self.positions.itemAtPosition(x, y).widget()
                print("HERE")
                if w.if_checking_mode:
                    w.is_checked = True
                    break
                if w.is_move and not w.is_checked:
                    if w.is_ship or w.is_anchor:
                        self.move.if_correct = False
                        # print("WRONG")
                        self.clear_move()
                        break
                    if self.move is None:
                        self.move = Move(x, y)
                    else:
                        self.move.add_info(x, y)
                        if not self.move.if_correct:
                            # print("WRONG")
                            self.clear_move()
                            break
                    w.is_checked = True

    def set(self):
        if self.move.if_correct:
            for x in range(0, self.dim):
                for y in range(0, self.dim):
                    w = self.positions.itemAtPosition(x, y).widget()
                    if w.is_checked:
                        w.is_ship = True
            self.put_anchors()
            self.clear_move()

    def clear_move(self):
        self.move = None
        for x in range(0, self.dim):
            for y in range(0, self.dim):
                w = self.positions.itemAtPosition(x, y).widget()
                w.is_move = False
                w.is_checked = False
                w.update()


    def show_anchors(self):
        if self.move.rotation == 'h':
            x_move = self.move.row
            y_move = self.move.column + self.move.number_of_decks - 1
        else:
            x_move = self.move.row + self.move.number_of_decks - 1
            y_move = self.move.column
        for x in range(self.move.row, x_move):
            for y in range(self.move.column, y_move):
                w = self.positions.itemAtPosition(y, x).widget()
                # if w.is_checked

    def if_unchecked_ships_around(self, w):
        for x in range(w.x - 1, w.x + 1):
            for y in range(w.y - 1, w.y + 1):
                if 0 <= x <= 9 and 0 <= y <= 9:
                    w = self.positions.itemAtPosition(x, y).widget()
                    if w.is_ship and not w.is_checked:
                        return False
        return True

    def find_ship(self, w):
        for x in range(w.x - 1, w.x + 1):
            for y in range(w.y - 1, w.y + 1):
                if 0 <= x <= 9 and 0 <= y <= 9:
                    w = self.positions.itemAtPosition(x, y).widget()
                    if w.is_ship:
                        return w
        return w


    def put_anchors(self):

        # w = self.positions.itemAtPosition(0, 0).widget()
        # if w.if_checking_mode:
        #     for x in range(0, self.dim):
        #         for y in range(0, self.dim):
        #             w = self.positions.itemAtPosition(x, y).widget()
        #             # f = self.if_checked_ships_around()
        #             # new_w = self.find_ship(w)
        #             for _ in range(9):
        #                 if self.if_unchecked_ships_around(w):
        #                     break
        #
        #                 w = self.find_ship(w)
        #                 if self.if_unchecked_ships_around(w):
        #                     break
        #
        #
        #                 if not self.if_unchecked_ships_around(w) and w.x == \
        #                         new_w.x and w.y == new_w.y:
        #                 new_w = self.find_ship(w)
        #                 if w.x == new_w.x and w.y == new_w.y:
        #                     break



        row = self.move.row
        col = self.move.column
        rotation = self.move.rotation
        size = self.move.number_of_decks

        if rotation == 'h':
            end_row = row
            end_col = col + size - 1
        else:
            end_row = row + size - 1
            end_col = col

        for x in range(col - 1, end_col + 2):
            for y in range(row - 1, end_row + 2):
                if 0 <= x <= 9 and 0 <= y <= 9:
                    w = self.positions.itemAtPosition(y, x).widget()
                    if not w.is_ship:
                        w.is_anchor = True

    def set_checking_mode(self):
        for x in range(0, self.dim):
            for y in range(0, self.dim):
                w = self.positions.itemAtPosition(x, y).widget()
                w.if_checking_mode = True

    #
    # def generate_random_field(self):
    #     pass
    #
    # def generate_user_field(self):
    #     while self.ship_factory.ships_1decks + self.ship_factory.ships_2decks + \
    #             self.ship_factory.ships_3decks + self.ship_factory.ships_4decks != 0:
    #         ship = self.ship_factory.get_a_ship()
    #         mes = ship.put_ship(self)
    #         if len(mes) != 0:
    #             while len(mes) != 0:
    #                 print(mes + ''' Давай попробуем ещё раз''')
    #                 ship = self.ship_factory.get_a_ship()
    #                 mes = ship.put_ship(self)
    #         ship.put_anchors(self.board)
    #         self.in_and_out.print_board(self.board)
    #
    # def compare_fields(self):
    #     pass
    #
    # def if_winner(self):
    #     pass

        # for h in range(row - 1, end_row + 2):
        #     for v in range(col - 1, end_col + 2):
        #         if self.move.if_correct() and field[h][v] != 1:
        #             field[h][v] = 2
