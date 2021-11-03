import math
import sys

from PyQt5 import QtCore, QtWidgets


class Ui_MYcalc(object):
    def setupUi(self, MYcalc):
        MYcalc.setObjectName("MYcalc")
        MYcalc.resize(414, 656)
        MYcalc.setFixedSize(414,656)
        MYcalc.setStyleSheet("background-color: rgb(85, 87, 83);")
        self.centralwidget = QtWidgets.QWidget(MYcalc)
        self.centralwidget.setObjectName("centralwidget")
        self.clear_button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_button.setGeometry(QtCore.QRect(10, 460, 71, 71))
        self.clear_button.setStyleSheet("background-color: rgb(204, 0, 0);")
        self.clear_button.setObjectName("clear_button")
        self.eq_button = QtWidgets.QPushButton(self.centralwidget)
        self.eq_button.setGeometry(QtCore.QRect(170, 540, 151, 71))
        self.eq_button.setStyleSheet("background-color: rgb(78, 154, 6);")
        self.eq_button.setObjectName("eq_button")
        self.lg_button = QtWidgets.QPushButton(self.centralwidget)
        self.lg_button.setGeometry(QtCore.QRect(10, 300, 71, 71))
        self.lg_button.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.lg_button.setObjectName("lg_button")
        self.minus_button = QtWidgets.QPushButton(self.centralwidget)
        self.minus_button.setGeometry(QtCore.QRect(330, 380, 71, 71))
        self.minus_button.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.minus_button.setObjectName("minus_button")
        self.div_button = QtWidgets.QPushButton(self.centralwidget)
        self.div_button.setGeometry(QtCore.QRect(330, 220, 71, 71))
        self.div_button.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.div_button.setObjectName("div_button")
        self.mult_button = QtWidgets.QPushButton(self.centralwidget)
        self.mult_button.setGeometry(QtCore.QRect(330, 300, 71, 71))
        self.mult_button.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.mult_button.setObjectName("mult_button")
        self.pm_button = QtWidgets.QPushButton(self.centralwidget)
        self.pm_button.setGeometry(QtCore.QRect(10, 380, 71, 71))
        self.pm_button.setStyleSheet("background-color: rgb(204, 0, 0);")
        self.pm_button.setObjectName("pm_button")
        self.dot_button = QtWidgets.QPushButton(self.centralwidget)
        self.dot_button.setGeometry(QtCore.QRect(10, 540, 71, 71))
        self.dot_button.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.dot_button.setObjectName("dot_button")
        self.plus_button = QtWidgets.QPushButton(self.centralwidget)
        self.plus_button.setGeometry(QtCore.QRect(330, 460, 71, 151))
        self.plus_button.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.plus_button.setObjectName("plus_button")
        self.button7 = QtWidgets.QPushButton(self.centralwidget)
        self.button7.setGeometry(QtCore.QRect(90, 460, 71, 71))
        self.button7.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.button7.setObjectName("button7")
        self.button8 = QtWidgets.QPushButton(self.centralwidget)
        self.button8.setGeometry(QtCore.QRect(170, 460, 71, 71))
        self.button8.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.button8.setObjectName("button8")
        self.button9 = QtWidgets.QPushButton(self.centralwidget)
        self.button9.setGeometry(QtCore.QRect(250, 460, 71, 71))
        self.button9.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.button9.setObjectName("button9")
        self.button6 = QtWidgets.QPushButton(self.centralwidget)
        self.button6.setGeometry(QtCore.QRect(250, 380, 71, 71))
        self.button6.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.button6.setObjectName("button6")
        self.button5 = QtWidgets.QPushButton(self.centralwidget)
        self.button5.setGeometry(QtCore.QRect(170, 380, 71, 71))
        self.button5.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.button5.setObjectName("button5")
        self.button4 = QtWidgets.QPushButton(self.centralwidget)
        self.button4.setGeometry(QtCore.QRect(90, 380, 71, 71))
        self.button4.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.button4.setObjectName("button4")
        self.button0 = QtWidgets.QPushButton(self.centralwidget)
        self.button0.setGeometry(QtCore.QRect(90, 540, 71, 71))
        self.button0.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.button0.setObjectName("button0")
        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.setGeometry(QtCore.QRect(90, 300, 71, 71))
        self.button1.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.button1.setObjectName("button1")
        self.button2 = QtWidgets.QPushButton(self.centralwidget)
        self.button2.setGeometry(QtCore.QRect(170, 300, 71, 71))
        self.button2.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.button2.setObjectName("button2")
        self.button3 = QtWidgets.QPushButton(self.centralwidget)
        self.button3.setGeometry(QtCore.QRect(250, 300, 71, 71))
        self.button3.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.button3.setObjectName("button3")
        self.square_button = QtWidgets.QPushButton(self.centralwidget)
        self.square_button.setGeometry(QtCore.QRect(250, 220, 71, 71))
        self.square_button.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.square_button.setObjectName("square_button")
        self.log_button = QtWidgets.QPushButton(self.centralwidget)
        self.log_button.setGeometry(QtCore.QRect(170, 220, 71, 71))
        self.log_button.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.log_button.setObjectName("log_button")
        self.root_button = QtWidgets.QPushButton(self.centralwidget)
        self.root_button.setGeometry(QtCore.QRect(90, 220, 71, 71))
        self.root_button.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.root_button.setObjectName("root_button")
        self.ln_button = QtWidgets.QPushButton(self.centralwidget)
        self.ln_button.setGeometry(QtCore.QRect(10, 220, 71, 71))
        self.ln_button.setStyleSheet("background-color: rgb(211, 215, 207);")
        self.ln_button.setObjectName("ln_button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 110, 381, 91))
        self.label.setStyleSheet("background-color: rgb(186, 189, 182);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 381, 91))
        self.label_2.setStyleSheet("background-color: rgb(186, 189, 182);")
        self.label_2.setObjectName("label_2")
        MYcalc.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MYcalc)
        self.statusbar.setObjectName("statusbar")
        MYcalc.setStatusBar(self.statusbar)
        self.retranslateUi(MYcalc)
        QtCore.QMetaObject.connectSlotsByName(MYcalc)


    def retranslateUi(self, MYcalc):
        _translate = QtCore.QCoreApplication.translate
        MYcalc.setWindowTitle(_translate("MYcalc", "Калькулятор"))
        self.clear_button.setText(_translate("MYcalc", "C"))
        self.eq_button.setText(_translate("MYcalc", "="))
        self.lg_button.setText(_translate("MYcalc", "e"))
        self.minus_button.setText(_translate("MYcalc", "-"))
        self.div_button.setText(_translate("MYcalc", "/"))
        self.mult_button.setText(_translate("MYcalc", "x"))
        self.pm_button.setText(_translate("MYcalc", "<"))
        self.dot_button.setText(_translate("MYcalc", "."))
        self.plus_button.setText(_translate("MYcalc", "+"))
        self.button7.setText(_translate("MYcalc", "7"))
        self.button8.setText(_translate("MYcalc", "8"))
        self.button9.setText(_translate("MYcalc", "9"))
        self.button6.setText(_translate("MYcalc", "6"))
        self.button5.setText(_translate("MYcalc", "5"))
        self.button4.setText(_translate("MYcalc", "4"))
        self.button0.setText(_translate("MYcalc", "0"))
        self.button1.setText(_translate("MYcalc", "1"))
        self.button2.setText(_translate("MYcalc", "2"))
        self.button3.setText(_translate("MYcalc", "3"))
        self.square_button.setText(_translate("MYcalc", "^"))
        self.log_button.setText(_translate("MYcalc", "log"))
        self.root_button.setText(_translate("MYcalc", "√"))
        self.ln_button.setText(_translate("MYcalc", "P"))
        self.label.setText(_translate("MYcalc", ""))
        self.label_2.setText(_translate("MYcalc", ""))


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MYcalc()
        self.ui.setupUi(self)
        self.ui.button0.clicked.connect(lambda: self.NumBut(0))
        self.ui.button1.clicked.connect(lambda: self.NumBut(1))
        self.ui.button2.clicked.connect(lambda: self.NumBut(2))
        self.ui.button3.clicked.connect(lambda: self.NumBut(3))
        self.ui.button4.clicked.connect(lambda: self.NumBut(4))
        self.ui.button5.clicked.connect(lambda: self.NumBut(5))
        self.ui.button6.clicked.connect(lambda: self.NumBut(6))
        self.ui.button7.clicked.connect(lambda: self.NumBut(7))
        self.ui.button8.clicked.connect(lambda: self.NumBut(8))
        self.ui.button9.clicked.connect(lambda: self.NumBut(9))
        self.ui.ln_button.clicked.connect(lambda: self.NumBut(3.14159))
        self.ui.lg_button.clicked.connect(lambda: self.NumBut(2.71828))
        self.ui.pm_button.clicked.connect(lambda: self.NumDel(float(self.ui.label_2.text())))
        self.ui.eq_button.clicked.connect(self.Ruvno)
        self.ui.clear_button.clicked.connect(self.Clear)
        self.ui.root_button.clicked.connect(self.NumRoot)
        self.ui.plus_button.clicked.connect(self.NumPlus)
        self.ui.minus_button.clicked.connect(self.NumMinus)
        self.ui.mult_button.clicked.connect(self.NumMult)
        self.ui.div_button.clicked.connect(self.NumDiv)
        self.ui.dot_button.clicked.connect(lambda : self.Dot((self.ui.label_2.text())))
        self.ui.log_button.clicked.connect(self.Log)
        self.ui.square_button.clicked.connect(self.Step)


    def Dot(self,num):
        r = 0
        v = str(num)
        l = len(v)
        if len(v) >= 2:
            if v.endswith('.'):
                v = v[0:len(v) - 2]
            else:
                r = v[:l - 1]
        else:
            r = v[:l - 1]
        self.ui.label_2.setText(str(r))


    def NumRoot(self):
        n = math.sqrt(int(self.ui.label_2.text()))
        self.ui.label.setText(str(n))
        self.ui.label_2.clear()


    def NumBut(self,num):
        v = str(num)
        self.ui.label_2.setText(self.ui.label_2.text()+v)


    def Ruvno(self):
        self.ui.label.setText(self.ui.label_2.text())
        self.ui.label_2.clear()

    def Clear(self):
        if len(self.ui.label_2.text()) !=0:
            self.ui.label_2.clear()
        else:
            self.ui.label.clear()


    def NumDel(self,num):
        v = str(num)
        l = len(v)
        r = 0
        if len(v) >= 2:
            if v.endswith('.'):
                v = v[0:len(v) - 2]
            else:
                r = v[:l - 1]
        else:
            r = v[:l - 1]
        self.ui.label_2.setText(r)


    def NumPlus(self):
        if len(self.ui.label.text()) == 0:
            self.ui.label.setText(self.ui.label_2.text())
            self.ui.label_2.clear()
        else:
            sum = float(self.ui.label.text()) + float(self.ui.label_2.text())
            self.ui.label.setText(str(sum))
            self.ui.label_2.clear()


    def NumMinus(self):
        if len(self.ui.label.text()) == 0:
            self.ui.label.setText(self.ui.label_2.text())
            self.ui.label_2.clear()
        else:
            sum = float(self.ui.label.text()) - float(self.ui.label_2.text())
            self.ui.label.setText(str(sum))
            self.ui.label_2.clear()


    def NumMult(self):
        if len(self.ui.label.text()) == 0:
            self.ui.label.setText(self.ui.label_2.text())
            self.ui.label_2.clear()
        else:
            sum = float(self.ui.label.text()) * float(self.ui.label_2.text())
            self.ui.label.setText(str(sum))
            self.ui.label_2.clear()


    def NumDiv(self):
        if len(self.ui.label.text()) == 0:
            self.ui.label.setText(self.ui.label_2.text())
            self.ui.label_2.clear()
        else:
            sum = float(self.ui.label.text()) / float(self.ui.label_2.text())
            self.ui.label.setText(str(sum))
            self.ui.label_2.clear()


    def Step(self):
        if len(self.ui.label.text()) == 0:
            self.ui.label.setText(self.ui.label_2.text())
            self.ui.label_2.clear()
        else:
            sum = float(self.ui.label.text()) ** float(self.ui.label_2.text())
            self.ui.label.setText(str(sum))
            self.ui.label_2.clear()


    def Log(self):
        if len(self.ui.label.text()) == 0:
            self.ui.label.setText(self.ui.label_2.text())
            self.ui.label_2.clear()
        else:
            sum = math.log(float(self.ui.label.text()), float(self.ui.label_2.text()))
            self.ui.label.setText(str(sum))
            self.ui.label_2.clear()


app = QtWidgets.QApplication([])
win = Window()
win.show()
sys.exit(app.exec_())
