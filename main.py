from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication 
#from qt_material import apply_stylesheet
#from PySide6 import QtWidgets
import sys

class LandingScreen(QtWidgets.QMainWindow):
    def __init__(self):
        super(LandingScreen, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi(r'src\ui\ui layout\landing screen.ui', self) # Load the .ui file
        self.pushButton.clicked.connect(self.loadMainwindow)
        #self.show() # Show the GUI

    def loadMainWindow(self):
        widget.setCurrentIndex(widget.currentIndex()+1)

    
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi(r'src\ui\ui layout\Final layout.ui', self) # Load the .ui file
        #self.show() # Show the GUI


app = QApplication(sys.argv)
#window = Ui()

widget = QtWidgets.QStackedWidget()
landing_screen = LandingScreen()
main_window = MainWindow()
widget.addWidget(landing_screen)
widget.add(main_window)


#apply_stylesheet(app, theme='dark_blue.xml')

widget.show()
app.exec_()