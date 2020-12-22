#Using Pyqt5
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 300, 300)
    win.setWindowTitle("PyQt Practice")
    
    label = QtWidgets.QLabel(win)
    label.setText("Initial label")
    label.move(50, 50)  
    
    win.show()
    sys.exit(app.exec_())
    
window()