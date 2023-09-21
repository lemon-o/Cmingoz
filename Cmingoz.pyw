import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QLineEdit, QPushButton, QMessageBox, QDesktopWidget
from PyQt5.QtGui import QIcon, QKeySequence, QIntValidator
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QFrame, QShortcut


class ConverterWidget(QWidget):
    def __init__(self):
        super().__init__()
        #设置窗口图标
        self.setWindowIcon(QIcon('./icon.png'))
        self.setWindowTitle("Cmingoz")
        FIXED_HEIGHT = 200
        INITIAL_WIDTH = 250
        screen_width = QApplication.primaryScreen().availableGeometry().width()  
        screen_height = QApplication.primaryScreen().availableGeometry().height()
        self.setMaximumHeight(FIXED_HEIGHT)
        self.setMinimumHeight(FIXED_HEIGHT)
        self.setMinimumWidth(INITIAL_WIDTH)
        self.resize(INITIAL_WIDTH, FIXED_HEIGHT)
        x = (screen_width - self.width()) / 2
        y = (screen_height - FIXED_HEIGHT) / 2
        self.move(int(x), int(y))

        linedit_style = 'background-color: white; color: #272727; border-radius: 6px; border: 1px solid #C5C5C5;'
        linedit_height = 22
        self.cm_input = QLineEdit()
        self.cm_input.setStyleSheet(linedit_style)
        self.cm_input.setFixedHeight(linedit_height)
        validator1 = QIntValidator()
        self.cm_input.setValidator(validator1)
        self.in_input = QLineEdit()
        self.in_input.setStyleSheet(linedit_style)
        self.in_input.setFixedHeight(linedit_height)
        validator2 = QIntValidator()
        self.in_input.setValidator(validator2)        
        self.g_input = QLineEdit()
        self.g_input.setStyleSheet(linedit_style)
        self.g_input.setFixedHeight(linedit_height)
        validator3 = QIntValidator()
        self.g_input.setValidator(validator3)
        self.oz_input = QLineEdit()
        self.oz_input.setStyleSheet(linedit_style)
        self.oz_input.setFixedHeight(linedit_height)
        validator4 = QIntValidator()
        self.oz_input.setValidator(validator4)

        label_style_1 = 'color: #3B3E41; margin-top: 0px; margin-bottom: 0px;'
        self.cm_label = QLabel("厘米")
        self.cm_label.setStyleSheet(label_style_1)
        self.equal2 = QLabel("=")
        self.equal2.setStyleSheet(label_style_1)
        self.in_label = QLabel("英寸")
        self.in_label.setStyleSheet(label_style_1)
        self.goz_result = QLabel()
        self.goz_result.setStyleSheet(label_style_1)
        self.g_label = QLabel("克")
        self.g_label.setStyleSheet(label_style_1)
        self.equal = QLabel("=")
        self.equal.setStyleSheet(label_style_1)
        self.oz_label = QLabel("盎司")
        self.oz_label.setStyleSheet(label_style_1)
        self.cmin_result = QLabel()
        self.cmin_result.setStyleSheet(label_style_1)

        button_style = """
        QPushButton {
            background-color: white;
            color: #3B3E41;
            border-radius: 10px;
            border: 1px solid #C5C5C5;
        }

        QPushButton:hover {
            background-color: #7DC9CA;
            border: 1px solid #397071;
        }
        """
        button_width1 = 110
        button_width2 = 105
        button_height1 = 26
        self.inch_copy_button = QPushButton("复制结果F1")
        self.inch_copy_button.setStyleSheet(button_style)
        self.inch_copy_button.setFixedSize(button_width2, button_height1)
        self.ounce_copy_button = QPushButton("复制结果F2")
        self.ounce_copy_button.setStyleSheet(button_style)
        self.ounce_copy_button.setFixedSize(button_width1, button_height1)

        self.convert_cm_to_inch()
        self.convert_inch_to_cm()
        self.convert_g_to_ounce()
        self.convert_ounce_to_g()

        self.cm_input.textChanged.connect(self.convert_cm_to_inch)
        self.in_input.textChanged.connect(self.convert_inch_to_cm)
        self.g_input.textChanged.connect(self.convert_g_to_ounce)
        self.oz_input.textChanged.connect(self.convert_ounce_to_g)

        self.inch_copy_button.clicked.connect(self.copy_cmin_result)
        self.ounce_copy_button.clicked.connect(self.copy_goz_result)

        inch_layout = QHBoxLayout()
        inch_layout.addWidget(self.cmin_result)
        inch_layout.addSpacing(10)
        inch_layout.addWidget(self.inch_copy_button)

        inch2_layout = QHBoxLayout()
        inch2_layout.addWidget(self.cm_input)
        inch2_layout.addWidget(self.cm_label)
        inch2_layout.addWidget(self.equal)
        inch2_layout.addWidget(self.in_input)
        inch2_layout.addWidget(self.in_label)

        ounce_layout = QHBoxLayout()
        ounce_layout.addWidget(self.goz_result)
        ounce_layout.addSpacing(0)
        ounce_layout.addWidget(self.ounce_copy_button)

        ounce2_layout = QHBoxLayout()
        ounce2_layout.addWidget(self.g_input)
        ounce2_layout.addWidget(self.g_label)
        ounce2_layout.addWidget(self.equal2)
        ounce2_layout.addWidget(self.oz_input)
        ounce2_layout.addWidget(self.oz_label)

        layout = QVBoxLayout()
        layout.addSpacing(12)
        layout.addLayout(inch2_layout)
        layout.addLayout(inch_layout)
        layout.addSpacing(36)
        layout.addLayout(ounce2_layout)
        layout.addLayout(ounce_layout)
        layout.addSpacing(12)

        self.setLayout(layout)

        self.hline = QFrame(self)
        self.hline.setFrameShape(QFrame.HLine) 
        self.hline.setFrameShadow(QFrame.Plain)
        self.y = 100  # 设置水平分隔线的位置
        self.hline.setGeometry(0, self.y, self.width(), 1) 
        self.hline.setStyleSheet("border: 1px solid #C5C5C5;")

        # Set window flags to stay on top
        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)

        self.shortcut_return = QShortcut(QKeySequence(Qt.Key_F1), self)
        self.shortcut_return.activated.connect(self.copy_cmin_result)
        self.shortcut_return = QShortcut(QKeySequence(Qt.Key_F2), self)
        self.shortcut_return.activated.connect(self.copy_goz_result)

    def resizeEvent(self, event):
        # 获取新的窗口宽度和高度
        new_width = event.size().width()
        new_height = event.size().height()
        # 将水平分隔线位置和大小设置为新的窗口宽度和高度
        self.hline.setGeometry(0, self.y, new_width, 1)

    def convert_cm_to_inch(self):
        text = self.cm_input.text()
        try:
            cm = float(text)
            inch = cm * 0.393701
            self.in_input.textChanged.disconnect()
            self.in_input.setText(f"{inch:.4f}")
            self.cmin_result.setText(f"{cm:.2f} cm / {inch:.2f} in")
            self.in_input.textChanged.connect(self.convert_inch_to_cm)
        except ValueError:
            self.cmin_result.setText("未输入换算数字")
            self.in_input.clear()

    def convert_inch_to_cm(self):
        text = self.in_input.text()
        try:
            inch = float(text)
            cm = inch / 0.393701
            self.cm_input.textChanged.disconnect()
            self.cm_input.setText(f"{cm:.4f}")
            self.cmin_result.setText(f"{inch:.2f} in / {cm:.2f} cm")
            self.cm_input.textChanged.connect(self.convert_cm_to_inch)
        except ValueError:
            self.cmin_result.setText("未输入换算数字")
            self.cm_input.clear()

    def convert_g_to_ounce(self):
        text = self.g_input.text()
        try:
            g = float(text)
            ounce = g * 0.035274
            self.oz_input.textChanged.disconnect()
            self.oz_input.setText(f"{ounce:.4f}")
            self.goz_result.setText(f"{g:.2f} g / {ounce:.2f} oz")
            self.oz_input.textChanged.connect(self.convert_ounce_to_g)
        except ValueError:
            self.goz_result.setText("未输入换算数字")
            self.oz_input.clear()

    def convert_ounce_to_g(self):
        text = self.oz_input.text()
        try:
            ounce = float(text)
            g = ounce / 0.035274
            self.g_input.textChanged.disconnect()
            self.g_input.setText(f"{g:.4f}")
            self.goz_result.setText(f"{ounce:.2f} oz / {g:.2f} g")
            self.g_input.textChanged.connect(self.convert_g_to_ounce)
        except ValueError:
            self.goz_result.setText("未输入换算数字")
            self.g_input.clear()

    def copy_cmin_result(self):
        if self.cmin_result.text() == "未输入换算数字":
            QMessageBox.information(self,'提示','请输入要换算的数字')
            return
        else:
            clipboard = QApplication.clipboard()
            result = self.cmin_result.text()
            clipboard.setText(result)
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Information) 
            msg.setWindowTitle("提示")
            msg.setText("复制成功! 将重置此换算。")
            QTimer.singleShot(1500, msg.close) 
            msg.exec_()
            self.cm_input.clear()
            self.in_input.clear()

        
    def copy_goz_result(self):
        if self.goz_result.text() == "未输入换算数字":
            QMessageBox.information(self,'提示','请输入要换算的数字')
            return
        else:
            clipboard = QApplication.clipboard()
            result = self.goz_result.text()
            clipboard.setText(result)
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Information) 
            msg.setWindowTitle("提示")
            msg.setText("复制成功! 将重置此换算。")
            QTimer.singleShot(1500, msg.close) 
            msg.exec_()
            self.g_input.clear()
            self.oz_input.clear()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    converter = ConverterWidget()
    converter.show()
    sys.exit(app.exec_())