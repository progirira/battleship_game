from PyQt5 import QtCore
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QHBoxLayout

from controller.game import Game
from model.shipfactory import ShipFactory
from view.elements_setter import ElementsSetter


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
        self.init_user_placement_window()#ships)

