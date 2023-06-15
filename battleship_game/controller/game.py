from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QPixmap, QBrush
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QHBoxLayout

from battleship_game.model.field import Field


class Game:
    def __init__(self, dim=None, if_with_timer=False):
        self.window = None
        self.if_with_computer = None

        self.dim = dim
        self.if_with_timer = if_with_timer

        self.player1_field = None
        self.player2_field = None
        self.if_random = None
        self.elems_setter = None
        self.ships_factory = None
        self.main_window = None

    def set_dim(self, dim):
        self.dim = dim

    def set_computer_mode(self, if_computer):
        self.if_with_computer = if_computer

    def set_mode_with_timer(self):
        self.if_with_timer = True

    def init_fields(self):
        self.player1_field = Field(int(self.dim))
        self.player2_field = Field(int(self.dim))

    def return_player2_field(self):
        return self.player2_field.positions

    def init_user_placement_window(self): #, ships):

        vb = QVBoxLayout()

        vb.addWidget(self.elems_setter.phrase('computers move',))
        # vb.addWidget(self.elems_setter.phrase(['ships balance',
        #                                        str(ships)],
        #                                       have_to_format=True))
        hb = QHBoxLayout()
        extra_vb = QVBoxLayout()
        extra_vb.addWidget(self.elems_setter.button('random put',
                                                    self.player2_field.set))
        extra_vb.addWidget(self.elems_setter.button('put',
                                                    self.player2_field.set))
        extra_vb.addWidget(self.elems_setter.button('clear',
                           self.player2_field.clear_move))
        hb.addLayout(extra_vb)
        hb.addLayout(self.return_player2_field())
        hb.setAlignment(Qt.AlignHCenter)
        vb.addLayout(hb)

        w = QWidget()
        w.setLayout(vb)
        self.main_window.setCentralWidget(w)
        self.main_window.show()




