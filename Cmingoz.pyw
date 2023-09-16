import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QLineEdit, QPushButton, QMessageBox, QDesktopWidget
from PyQt5.QtGui import QClipboard, QIcon
from PyQt5.QtCore import Qt


class ConverterWidget(QWidget):
    def __init__(self):
        super().__init__()
        #设置窗口图标
        self.setWindowIcon(QIcon('./icon.png'))
        self.setWindowTitle("Cmingoz")
        self.resize(300, 200)
        self.center_window()

        self.cm_input = QLineEdit()
        self.inch_result = QLabel()
        self.inch_copy_button = QPushButton("复制结果")
        self.g_input = QLineEdit()
        self.ounce_result = QLabel()
        self.ounce_copy_button = QPushButton("复制结果")

        self.convert_cm_to_inch()
        self.convert_g_to_ounce()

        self.cm_input.textChanged.connect(self.convert_cm_to_inch)
        self.g_input.textChanged.connect(self.convert_g_to_ounce)

        self.inch_copy_button.clicked.connect(self.copy_inch_result)
        self.ounce_copy_button.clicked.connect(self.copy_ounce_result)

        inch_layout = QHBoxLayout()
        inch_layout.addWidget(self.inch_result)
        inch_layout.addWidget(self.inch_copy_button)

        ounce_layout = QHBoxLayout()
        ounce_layout.addWidget(self.ounce_result)
        ounce_layout.addWidget(self.ounce_copy_button)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("厘米转英寸:"))
        layout.addWidget(self.cm_input)
        layout.addLayout(inch_layout)
        layout.addWidget(QLabel("克转盎司:"))
        layout.addWidget(self.g_input)
        layout.addLayout(ounce_layout)

        self.setLayout(layout)

        # Set window flags to stay on top
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)

    def center_window(self):
        screen = QDesktopWidget().screenGeometry()
        window = self.geometry()
        x = (screen.width() - window.width()) // 2
        y = (screen.height() - window.height()) // 2
        self.move(x, y)

    def convert_cm_to_inch(self):
        text = self.cm_input.text()
        try:
            cm = float(text)
            inch = cm * 0.393701
            self.inch_result.setText(f"{cm} cm / {inch:.2f} in")
        except ValueError:
            self.inch_result.setText("请输入有效的数字")

    def convert_g_to_ounce(self):
        text = self.g_input.text()
        try:
            g = float(text)
            ounce = g * 0.035274
            self.ounce_result.setText(f"{g} g / {ounce:.2f} oz")
        except ValueError:
            self.ounce_result.setText("请输入有效的数字")

    def copy_inch_result(self):
        clipboard = QApplication.clipboard()
        result = self.inch_result.text()
        clipboard.setText(result)
        QMessageBox.information(self, "提示", "复制成功！")

    def copy_ounce_result(self):
        clipboard = QApplication.clipboard()
        result = self.ounce_result.text()
        clipboard.setText(result)
        QMessageBox.information(self, "提示", "复制成功！")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    converter = ConverterWidget()
    converter.show()
    sys.exit(app.exec_())