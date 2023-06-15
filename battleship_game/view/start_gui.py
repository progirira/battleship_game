from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import Qt
# from PyQt5.QtGui import *
from PyQt5.QtGui import QImage, QIcon, QPalette, QBrush, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, \
    QLabel

from battleship_game.controller.computer_game import ComputerGame
from battleship_game.controller.game import Game
from battleship_game.controller.hotspot_game import HotSpotGame
from battleship_game.view.elements_setter import ElementsSetter


IMG_BOMB = QImage("images/bomb.png")
IMG_SHIP = QImage("images/ship.png")
IMG_EMPTY = QImage("images/empty.png")


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.elems_setter = ElementsSetter()
        self.game = Game()

        pal = QPalette()

        pal.setBrush(QPalette.Background, QBrush(QPixmap("images\port.png")))

        self.setPalette(pal)

        self.setGeometry(QtCore.QRect(150, 80, 1600, 900))
        self.controller()

    def controller(self):
        self.game = Game()
        self.init_welcome_window()

    def init_welcome_window(self):
        vb = QVBoxLayout()
        vb.addWidget(self.elems_setter.phrase('hello',
                                              align_h=Qt.AlignHCenter,
                                              align_v=Qt.AlignCenter))

        vb.addWidget(self.elems_setter.phrase('choose mode',
                                              align_h=Qt.AlignLeft,
                                              align_v=Qt.AlignLeft))
        check_layout = QVBoxLayout()
        check_layout.addWidget(self.elems_setter.checkbox('computer mode', x=90, y=400,
                                                width=self.frameGeometry().width(),
                                                to_do=self.start_game_with_computer))
        check_layout.addWidget(self.elems_setter.checkbox('hot seat', x=90, y=600,
                                                width=self.frameGeometry().width(),
                                                to_do=self.init_window_choose_timer_mode))
        w = QWidget()
        # check_layout.setMargin(100)
        check_layout.setSpacing(100)

        vb.addLayout(check_layout)

        w.setLayout(vb)
        # w.setGeometry(0, 0, 200, 80)

        self.setCentralWidget(w)
        self.show()

    def start_game_with_computer(self):
        self.game.set_computer_mode(True)
        self.choose_dim()
        # self.init_ships_placement_window('computer places')

    def init_window_choose_timer_mode(self):
        self.game.set_computer_mode(False)
        vb = QVBoxLayout()

        vb.addWidget(self.elems_setter.phrase('choose timer mode',
                                              align_h=Qt.AlignLeft,
                                              bold=60))
        vb.addWidget(self.elems_setter.checkbox('with timer', x=90, y=400,
                                                width=self.frameGeometry().width(),
                                                to_do=self.set_mode_with_timer))
        vb.addWidget(self.elems_setter.checkbox('non-timer mode', x=90, y=600,
                                                width=self.frameGeometry().width(),
                                                to_do=self.choose_dim))
        w = QWidget()
        w.setLayout(vb)

        self.setCentralWidget(w)
        self.show()

    def set_mode_with_timer(self):
        self.game.set_mode_with_timer()
        self.choose_dim()

    def choose_dim(self):
        vb = QVBoxLayout()

        # Просим начать расставлять
        vb.addWidget(self.elems_setter.phrase('choose dim',
                                              align_h=Qt.AlignLeft,
                                              bold=60))

        vb.addWidget(
            self.elems_setter.combo_box(arr_of_choices=["", "10", "15", "20"],
                                        to_do=self.set_game, x=90, y=400,
                                        width=self.frameGeometry().width()))

        w = QWidget()
        print("HERE")

        w.setLayout(vb)
        self.setCentralWidget(w)

        self.show()

    def set_game(self, dim):
        self.game.set_dim(dim)
        if self.game.if_with_computer:
            self.game = ComputerGame(main_window=self, dim=self.game.dim,
                                     if_with_timer=self.game.if_with_timer)
        else:
            self.game = HotSpotGame(main_window=self, dim=self.game.dim,
                                    if_with_timer=self.game.if_with_timer)


if __name__ == '__main__':
    app = QApplication([])
    windows = MainWindow()
    app.exec_()
