"""main_window.py"""
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QLabel, QVBoxLayout, QComboBox, QStyleFactory
from PyQt5.QtCore import Qt
from compactness import Compactness

APP_TITLE = 'Py Compactness'
MIN_WIDTH = 300
MIN_HEIGHT = 200


class MainWindow(QMainWindow):
    """Presents result of calculcation of compactness and processed image"""

    def __init__(self):
        super().__init__()
        self.compactness = Compactness(image_name="arrow.jpg")
        self.setWindowTitle(APP_TITLE)
        self.__calculate_window_size()
        self.general_layout = self.__setup_general_layout("arrow.jpg")
        self._central_widget = QWidget(self)
        self.setCentralWidget(self._central_widget)
        self._central_widget.setLayout(self.general_layout)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet("background-color: rgba(0, 41, 59, 255)")

    def __calculate_window_size(self, resolution=None):
        if resolution:
            self.setMinimumWidth(resolution.width() / 3)
            self.setMinimumHeight(resolution.height() / 1.5)
        else:
            self.setMinimumWidth(MIN_WIDTH)
            self.setMinimumHeight(MIN_HEIGHT)

    def __setup_general_layout(self, image):
        layout = QHBoxLayout()
        layout.addLayout(self.__setup_left_part_of_layout())
        layout.addLayout(self.__setup_right_part_of_layout(image))
        return layout

    def __setup_left_part_of_layout(self):
        left_layout = QVBoxLayout()
        self.type_combo_box = QComboBox()
        self.__setup_background_color_for_widget(self.type_combo_box)
        self.type_combo_box.addItems(["P2A",
                                      "Isoperimetric ratios",
                                      "Shape to minimal circle on shape",
                                      "Circle with the same area as shape"])
        self.type_combo_box.activated[str].connect(self.__change_type_and_result)
        image_combo_box = QComboBox()
        self.__setup_background_color_for_widget(image_combo_box)
        image_combo_box.addItems(["Arrow",
                                  "Circle",
                                  "Square",
                                  "Polygon",
                                  "Inregular shape",
                                  "Inregular shape 2",
                                  "Triangle",
                                  "Trapezoid"])
        image_combo_box.activated[str].connect(self.__change_image)
        self.type_label = QLabel('P2A')
        self.__setup_background_color_for_widget(self.type_label)
        self.result_label = QLabel(f'{self.compactness.p2a}')
        self.__setup_background_color_for_widget(self.result_label)
        left_layout.addWidget(self.type_combo_box)
        left_layout.addWidget(image_combo_box)
        left_layout.addWidget(self.type_label)
        left_layout.addWidget(self.result_label)
        return left_layout

    def __setup_right_part_of_layout(self, image):
        right_layout = QVBoxLayout()
        self.right_label = QLabel(self)
        pixmap = QPixmap(image)
        self.right_label.resize(150, 150)
        self.right_label.setPixmap(pixmap.scaled(self.right_label.size(), Qt.IgnoreAspectRatio))
        right_layout.addWidget(self.right_label)
        return right_layout

    @staticmethod
    def __setup_background_color_for_widget(widget):
        """Setup app style background for widgets"""
        widget.setAttribute(Qt.WA_StyledBackground, True)
        widget.setStyleSheet("background-color: white;")

    def __change_type_and_result(self, for_name):
        if for_name == 'P2A':
            self.type_label.setText('P2A')
            self.result_label.setText(f'{self.compactness.p2a}')
        elif for_name == 'Isoperimetric ratios':
            self.type_label.setText('Isoperimetric ratios')
            self.result_label.setText(f'{self.compactness.iso_ration}')
        elif for_name == 'Shape to minimal circle on shape':
            self.type_label.setText('Shape to minimal circle on shape')
            self.result_label.setText(f'{self.compactness.min_circle_comp}')
        elif for_name == 'Circle with the same area as shape':
            self.type_label.setText('Circle with the same area as shape')
            self.result_label.setText(f'{self.compactness.equal_fields_comp}')

    def __change_image(self, option_name):
        image_name = ""

        if option_name == 'Arrow':
            image_name = "arrow.jpg"
        elif option_name == 'Circle':
            image_name = "circle.png"
        elif option_name == 'Square':
            image_name = "square.png"
        elif option_name == 'Polygon':
            image_name = "polygon.png"
        elif option_name == 'Inregular shape':
            image_name = "inregular_shape.png"
        elif option_name == 'Inregular shape 2':
            image_name = 'inregular_shape_2.png'
        elif option_name == 'Triangle':
            image_name = 'triangle.png'
        elif option_name == 'Trapezoid':
            image_name = 'trapezoid.png'

        self.compactness = Compactness(image_name=image_name)
        self.type_label.setText('P2A')
        self.result_label.setText(f'{self.compactness.p2a}')
        self.type_combo_box.setCurrentIndex(0)
        pixmap = QPixmap(image_name)
        self.right_label.resize(150, 150)
        self.right_label.setPixmap(pixmap.scaled(self.right_label.size(), Qt.IgnoreAspectRatio))
