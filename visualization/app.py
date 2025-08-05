import sys

from PyQt6.QtWidgets import QApplication, QWidget, QToolTip, QPushButton
from PyQt6.QtGui import QFont


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')

        btu = QPushButton("button", self)
        # noinspection PyUnresolvedReferences
        btu.clicked.connect(QApplication.instance().quit)
        btu.setToolTip("This is a <b>QPushButton</b> widget QUIT")
        btu.resize(btu.sizeHint())
        btu.move(50,50)

        self.setGeometry(300,300,300,200)
        self.setWindowTitle("Tooltips")
        self.show()

        ...


def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())
    # app = QApplication(sys.argv)
    #
    # windows = QWidget()
    #
    # windows.resize(600, 600)
    # windows.move(100, 30)
    #
    # windows.setWindowTitle("Simple")
    #
    # windows.show()
    #
    # sys.exit(app.exec())


if __name__ == '__main__':
    main()
