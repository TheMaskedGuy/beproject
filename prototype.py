from PyQt5 import QtWidgets, uic
from pynput.keyboard import Key, Controller
import sys

keyboard = Controller()

class Ui(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('prototype.ui', self)
        self.setWindowTitle('Prototype')


        #Button Linking
        self.btnTest1Passed.clicked.connect(lambda: self.btnPressed("Test-1 Passed!"))

        self.btnTest2Test.clicked.connect(lambda: self.btnPressed("Test-2"))
        self.btnTest2Passed.clicked.connect(lambda: self.btnPressed(" Passed!"))

        self.btnTest3T.clicked.connect(lambda: self.btnPressed("T"))
        self.btnTest3S.clicked.connect(lambda: self.btnPressed("S"))
        self.btnTest3E.clicked.connect(lambda: self.btnPressed("E"))
        self.btnTest3T_2.clicked.connect(lambda: self.btnPressed("T"))
        self.btnTest3P.clicked.connect(lambda: self.btnPressed(" P"))
        self.btnTest3E_2.clicked.connect(lambda: self.btnPressed("E"))
        self.btnTest3A.clicked.connect(lambda: self.btnPressed("A"))
        self.btnTest3S_2.clicked.connect(lambda: self.btnPressed("S"))
        self.btnTest3Exclaim.clicked.connect(lambda: self.btnPressed("!"))
        self.btnTest3D.clicked.connect(lambda: self.btnPressed("D"))
        self.btnTest3S_3.clicked.connect(lambda: self.btnPressed("S"))
        self.btnTest3num3.clicked.connect(lambda: self.btnPressed("3"))

        self.show()


    def btnPressed(self, keySymbol):
        print('Pressed Key: ' + keySymbol)
        

        key = keySymbol.strip()
        if len(key)<2:
            keyboard.press(key)
            keyboard.release(key)
        else:
            self.textEdit.insertPlainText(keySymbol)
            # self.textEdit.setText(keySymbol)



app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
