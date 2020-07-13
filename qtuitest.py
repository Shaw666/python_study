import sys
from PyQt5.QtWidgets import QApplication, QWidget


if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(1920, 1080)
    w.setWindowTitle("神秘的小东西开始吧！")
    w.show()

    sys.exit(app.exec_())