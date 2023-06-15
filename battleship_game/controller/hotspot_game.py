from battleship_game.controller.game import Game


class HotSpotGame(Game):
    def __init__(self, main_window, dim, if_with_timer):
        self.main_window = main_window
        self.dim = dim
        self.if_with_timer = if_with_timer
        super(Game, self).__init__()
        self.start()

    def start(self):
        print("HOTSPOT")
