from PySide6.QtWidgets import *
from PySide6.QtGui import *

import json

from demo import Ui_Form

dictionary: dict
index = 0


class Window(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.in_dict)

        shortcut = QShortcut(QKeySequence("Return"), self)
        shortcut.activated.connect(self.check)

        try:
            self.cn: list = list(dictionary.items())
            self.en: list = list(dictionary.keys())
        except NameError:
            pass

        self.refresh()

    def refresh(self):
        global index
        try:
            self.label.setText(dictionary.get(self.en[index]))
        except IndexError:
            self.label.setText("finish")
        except NameError:
            pass

    def check(self):
        global index
        # 获取输入文本
        text = self.lineEdit.text()
        if text == self.en[index]:
            print("正确")
            self.lineEdit.setText("")
            index += 1
            self.refresh()
        else:
            print("错误")
            self.lineEdit.setText("")

    def in_dict(self):
        global dictionary
        filePath,_ = QFileDialog.getOpenFileName(
            self,  # 父窗口对象
            "选择词库json",  # 标题
            r"./",  # 起始目录
            "奖杯 (*.json)"  # 选择类型过滤项，过滤内容在括号中
        )
        # self.line1.setText(filePath)
        print(filePath)
        with open(filePath, "r", encoding="utf-8") as f:
            r = str(f.read(-1))
            dictionary = dict(json.loads(r))
            print(dictionary)

        self.cn: list = list(dictionary.items())
        self.en: list = list(dictionary.keys())

        self.refresh()


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()
