import json

class In_and_out():
    def __init__(self):
        self.filename = "json_data.json"
        self.data = None

    def write_to_json(self):
        # print(pathlib.Path.cwd())
        data = {'hello': 'Привет! Предлагаю сыграть в морской бой:)',
                'choose mode': 'Выбери режим игры:',
                'computer mode': 'с компьютером в качестве соперника',
                'hot seat': 'с другом на одном компьютере',
                'fail': 'О нет! Ты повержен\nСыграем ещё?',
                'win': 'Этот бой оказался тебе по плечу!\nСыграем ещё раз?',
                'place ships': 'Расставь корабли:',
                'computer places': 'Я уже расставил свои корабли, теперь твоя '
                                 'очередь:\nВыбери клетки корабля и '
                                  'нажми поставить корабль',
                'computers move': 'Я уже сделал свой ход, '
                                  'ты следующий:',
                'start game': 'Начнём игру! Нанеси удар',
                'first gamer places': 'Первый игрок, расставь свои корабли!',
                'second gamer places': 'А теперь ты расставь свои корабли!',
                "first's move": 'Ход первого игрока',
                "second's move": 'Ход второго игрока',
                'first wins': 'Первый оказался в этот раз сильнее',
                'second wins': 'Второй выиграл!',
                'choose dim': 'Выберите размер поля:',
                'ships balance': 'Нужно расставить {} кораблей',
                'choose timer mode': 'Выбери, хочешь ли ты играть на время:',
                'with timer': 'с таймером',
                'non-timer mode': 'без таймера',
                'put': ' поставить корабль',
                'clear': ' стереть ',
                'random put': 'расставить рандомно все корабли'
                }
        json_string = json.dumps(data)
        with open(self.filename, 'w') as outfile:
            outfile.write(json_string)

    def load_data_from_json(self):
        with open(self.filename, 'r') as infile:
            self.data = json.load(infile)
        # for key in self.data.keys():
        #     print(key + " - " + self.data[key])
        # print(self.data)

    def read_from_json(self, key):
        if self.data is None:
            self.load_data_from_json()
        return self.data[key]


if __name__ == '__main__':
    in_out = In_and_out()
    in_out.write_to_json()

    in_out.load_data_from_json()


