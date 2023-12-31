from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget

from battleship_game.controller.game import Game
from battleship_game.model.shipfactory import ShipFactory
from battleship_game.view.elements_setter import ElementsSetter


class ComputerGame(Game):
    have_to_set = pyqtSignal()

    def __init__(self, main_window, dim, if_with_timer):
        self.main_window = main_window
        self.dim = dim
        self.if_with_timer = if_with_timer

        super(Game, self).__init__()
        self.elems_setter = ElementsSetter()
        self.ships_factory = ShipFactory()
        self.start()

    def start(self):
        self.init_fields()
        ships = self.ships_factory.return_num_of_ships()
        self.init_user_placement_window(8)
        # self.player2_field.setted.connect(self.start_playing)

    def init_user_placement_window(self, ships):
        vb = QVBoxLayout()

        vb.addWidget(self.elems_setter.phrase('computer places'))
        vb.addWidget(self.elems_setter.phrase(['ships balance',
                                               str(ships)],
                                              have_to_format=True))
        hb = QHBoxLayout()
        extra_vb = QVBoxLayout()
        # extra_vb.addWidget(self.elems_setter.button('random put',
        #                    self.random_set))
        extra_vb.addWidget(self.elems_setter.button('put',
                                                    self.set))
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

    def random_set(self):
        while self.ships_factory.amount != 0:
            self.player2_field.generate_random_set()
            self.set()

    def set(self):
        self.player2_field.set()
        self.ships_factory.decrease_amount()
        print(self.ships_factory.amount)
        if self.ships_factory.amount == 0:
            self.player2_field.set_checking_mode()
            self.start_playing()

    def start_playing(self):
        vb = QVBoxLayout()

        vb.addWidget(self.elems_setter.phrase('computers move'))

        hb = QHBoxLayout()
        extra_vb = QVBoxLayout()
        hb.addLayout(extra_vb)
        # hb.addLayout(self.return_player2_field())
        hb.addLayout(self.return_player1_field())
        hb.setAlignment(Qt.AlignHCenter)
        vb.addLayout(hb)

        w = QWidget()
        w.setLayout(vb)
        self.main_window.setCentralWidget(w)
        self.main_window.show()

