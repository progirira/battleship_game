from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QPushButton, QComboBox, QCheckBox

from view.in_and_out import In_and_out


class ElementsSetter:
    def __init__(self):
        self.storage = In_and_out()

    def phrase(self, lines, have_to_format=False,
                   align_h=Qt.AlignHCenter,
                   align_v=Qt.AlignVCenter,
                   point_size=22, bold=60):
        phrase = QLabel()
        phrase.setAlignment(align_h)
        phrase.setAlignment(align_v)

        f = phrase.font()
        f.setPointSize(point_size)
        f.setWeight(bold)
        phrase.setFont(f)
        if have_to_format:
            phrase.setText(self.storage.read_from_json(lines[0]).format(str(
                lines[1])))
            print(self.storage.read_from_json(lines[0]).format(str(
                lines[1])))
        else:
            phrase.setText(self.storage.read_from_json(lines))

        return phrase

    def button(self, text, to_do, point_size=18, bold=60):
        button = QPushButton(text)
        button.clicked.connect(to_do)

        f = button.font()
        f.setPointSize(point_size)
        f.setWeight(bold)
        button.setFont(f)
        button.setText(self.storage.read_from_json(text))
        return button

    def checkbox(self, text, x, y, width, to_do, height=100, \
                     point_size=22, bold=60,
                     ):
        check_box = QCheckBox(text)
        f = check_box.font()
        f.setPointSize(point_size)
        f.setWeight(bold)
        check_box.setFont(f)

        check_box.setCheckState(Qt.CheckState.Unchecked)
        if to_do is not None:
            check_box.stateChanged.connect(to_do)
        check_box.setGeometry(x, y, width, height)

        return check_box
    def combo_box(self, arr_of_choices, to_do, x, y, width, height=100):
        combo_box = QComboBox()
        combo_box.addItems(arr_of_choices)
        combo_box.currentTextChanged.connect(to_do)
        combo_box.setGeometry(x, y, width, height)

        return combo_box