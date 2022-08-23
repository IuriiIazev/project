import sys
from PyQt5 import QtWidgets, uic
import csv

fieldnames = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
main_list = []
s1 = []
s2 = []
numbers = []

with open("C:/Users/yuray/Downloads/Telegram Desktop/record2.csv", encoding='utf-8') as r_file:
    file_reader = csv.DictReader(r_file, fieldnames=fieldnames)
    for row in file_reader:
        s1.append(float(row[1]))
        s2.append(float(row[12]))

ss1 = s1[:17000]
ss2 = s2[:17000]

for m in range(len(ss1)):
    numbers.append(m)


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        uic.loadUi("C:/Users/yuray/Downloads/Telegram Desktop/base.ui", self)

        self.pushButton.clicked.connect(self.nazhatie_knopki)
        self.horizontalSlider.valueChanged.connect(self.changeValue)

        self.PlotWidget.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [30, 32, 34, 32, 33, 31, 29, 32, 35, 45])
        self.PlotWidget_2.plot([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [30, 32, 34, 32, 33, 31, 29, 32, 35, 45])

    def nazhatie_knopki(self):
        self.PlotWidget.clear()
        self.PlotWidget_2.clear()
        self.PlotWidget.plot(numbers, ss1)
        self.PlotWidget_2.plot(numbers, ss2)

    def changeValue(self,value):
        ss1 = s1[:int(value)]
        ss2 = s2[:int(value)]

    def check(self):
        while True:
         self.horizontalSlider.valueChanged.connect(self.changeValue)




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
