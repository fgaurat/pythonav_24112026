from pprint import pprint
from PySide6.QtWidgets import QApplication,QMainWindow
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

from main_window import Ui_MainWindow


class MainWindowApp(Ui_MainWindow, QMainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.click)

    def click(self):
        print('click')
        
        
        
def main_xml_ui():
    ui_file_name = "main.ui"
    
    app = QApplication([])
    
    ui_file = QFile(ui_file_name)
    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()

    window.show()
    app.exec()

def main():
    app = QApplication([])

    window = MainWindowApp()
    window.show()

    app.exec()

    
if __name__=='__main__':
    main()


