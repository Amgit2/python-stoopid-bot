#from yahoo_finance import Share
import yfinance as yf
import matplotlib as plt
plt.use('QT5Agg')

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QTableView, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, QAbstractTableModel, Qt

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

import sys

class graph(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(graph, self).__init__(fig)

def stonk(text):
    stock = yf.Ticker(text)
    stonk_df =stock.history(period = "max")
    print(stonk_df)
    return stonk_df


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 textbox - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 140
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280, 40)

        # Create a button in the window
        self.button = QPushButton('Show text', self)
        self.button.move(20, 80)

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)


    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        df = stonk(textboxValue)
        plot = graph(self, width = 5, height = 4, dpi = 100)
        df[["Open","Close"]].plot(ax = plot.axes)
        self.setCentralWidget((plot))
        #self.g = graph(plot)
        #self.g.show()



        #self.dialog = graph(plot)
        #self.dialog.show()
        #QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + df, QMessageBox.Ok)
        #self.textbox.setText("")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())

