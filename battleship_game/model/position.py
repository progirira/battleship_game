from PyQt5.QtCore import pyqtSignal, Qt, QSize
from PyQt5.QtGui import QImage, QPainter, QPalette, QBrush, QPixmap
from PyQt5.QtWidgets import QWidget

IMG_SHIP = QImage(r"..\view\images\ship.png")
IMG_ANCHOR = QImage(r"..\view\images\anchor.png")
IMG_BOMB = QImage(r"..\view\images\bomb.png")


class Position(QWidget):

    clicked = pyqtSignal()

    def __init__(self, x, y, *args, **kwargs):
        super(Position, self).__init__(*args, **kwargs)

        self.if_checking_mode = False
        self.is_ship = False
        self.is_move = False
        self.is_checked = False
        self.is_anchor = False
        self.setFixedSize(QSize(40, 40))
        self.update()

        self.x = x
        self.y = y

    def reset(self):

        self.update()

    def paintEvent(self, event):
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing)

        r = event.rect()
        if self.is_ship:
            color = self.palette().color(QPalette.Background)
            outer, inner = color, color
        else:
            outer, inner = Qt.gray, Qt.lightGray

        p.fillRect(r, QBrush(inner))

        if not self.if_checking_mode:
            if self.is_ship:
                p.drawPixmap(r, QPixmap(IMG_SHIP))
            elif self.is_anchor:
                p.drawPixmap(r, QPixmap(IMG_ANCHOR))
            elif self.is_move:
                p.drawPixmap(r, QPixmap(IMG_SHIP))

        else:
            if self.is_ship and self.is_checked:
                    p.drawPixmap(r, QPixmap(IMG_BOMB))
            elif self.is_anchor and self.is_checked:
                p.drawPixmap(r, QPixmap(IMG_ANCHOR))

    def click(self):

        self.is_move = True

        self.update()
        self.clicked.emit()

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.click()
