from PyQt5.QtWidgets import QApplication
from main_window import MainWindow
import sys


def main():
    """Actions to do when the application starts"""
    py_app = QApplication([])
    view = MainWindow()
    view.show()
    sys.exit(py_app.exec_())


if __name__ == '__main__':
    main()