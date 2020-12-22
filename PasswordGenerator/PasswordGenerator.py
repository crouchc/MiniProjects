#Password Generator Mini Project

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from random import randint

def passGen():
    specChars = "!@#$%^&*()_+{}:<>?"
    specCharsLen = len(specChars)
    nums = "1234567890"
    numsLen = len(nums)
    chars = "qwertyuiopasdfghjklzxcvbnm"
    charsLen = len(chars)
    password = ""
    
    while len(password) < 15:
        val = randint(1,3) #randomizes whether character will be special, number, or letter
        #Randomizes which special, number, or letter is placed in password
        if val == 1: 
            ind = randint(0,specCharsLen-1)
            password = password + specChars[ind]
        elif val == 2:
            ind = randint(0,numsLen-1)
            password = password + nums[ind]
        else:
              ind = randint(0,charsLen-1)
              password = password + chars[ind]
    print(password)
    return password
    input()
    
def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 300, 200)
    win.setWindowTitle("Password Generator")
    
    label = QtWidgets.QLabel(win)
    label.setText("Password:\n" + passGen())
    label.resize(100, 50)
    
    
    win.show()
    sys.exit(app.exec_())
    
window()
#Add storage of passwords with username and website name



    
