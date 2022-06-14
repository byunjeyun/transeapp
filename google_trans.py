import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import googletrans

form_class = uic.loadUiType('ui/google.ui')[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__() # 부모의 초기화자 호출
        self.setupUi(self) #제작해 놓은 google.ui를 연결
        self.setWindowTitle("구글 한줄 번역기")
        self.setWindowIcon(QIcon('icons/google.png'))
        self.statusBar().showMessage('google Trans App ver. 1.0')

        self.trans_btn.clicked.connect(self.trans_operation)
        self.reset_btn.clicked.connect(self.reset_operation)

    def trans_operation(self):
        trans = googletrans.Translator()
        ori_str = self.input_kor_text.text()

        trans_en = trans.translate(ori_str, dest='en')
        trans_jp = trans.translate(ori_str, dest='ja')
        trans_cn = trans.translate(ori_str, dest='zh-cn')

        self.output_en_text.append(trans_en.text)
        self.output_jp_text.append(trans_jp.text)
        self.output_cn_text.append(trans_cn.text)


    def reset_operation(self):
        self.input_kor_text.clear()
        self.output_en_text.clear()
        self.output_jp_text.clear()
        self.output_cn_text.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWindow()
    ex.show()
    sys.exit(app.exec_())