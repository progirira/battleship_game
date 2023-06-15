class ShipFactory(object):
    def __init__(self):
        self.ships_1decks = 4
        self.ships_2decks = 3
        self.ships_3decks = 2
        self.ships_4decks = 1

    def return_num_of_ships(self):
        return self.ships_1decks + self.ships_2decks + self.ships_3decks \
                + self.ships_4decks

    def if_free_ship_and_change(self, number_of_decks):
        match number_of_decks:
            case 1:
                if self.ships_1decks > 0:
                    self.ships_1decks -= 1
                    return True
            case 2:
                if self.ships_2decks > 0:
                    self.ships_2decks -= 1
                    return True
            case 3:
                if self.ships_3decks > 0:
                    self.ships_3decks -= 1
                    return True
            case 4:
                if self.ships_4decks > 0:
                    self.ships_4decks -= 1
                    return True
        return False
