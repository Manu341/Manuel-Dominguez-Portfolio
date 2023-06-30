import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QPushButton,QFormLayout
from newfile2 import *
from tes2 import *

class MyWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.setFixedSize(500,350)
        
        self.line_edit_a = QLineEdit()
        self.line_edit_b = QLineEdit()
        self.line_edit_c= QLineEdit()
        self.line_edit_d= QLineEdit()
        self.line_edit_e= QLineEdit()
        self.button = QPushButton('Continue')
        self.button.clicked.connect(self.create_CSV)
        self.button1=QPushButton("Analyze")
        self.button1.clicked.connect(self.analyze)
        self.warning=QLabel("No se olvide de modificar el CSV antes de analizar!")

        layout = QFormLayout()
        layout.addRow("Nombre del archivo:",self.line_edit_a)
        layout.addRow("Cantidad de paginas a leer:",self.line_edit_b)
        layout.addRow("Numero primera pagina:",self.line_edit_c)
        layout.addRow("Numero ultima pagina:",self.line_edit_d)
        layout.addRow("Nombre nuevo archivo:",self.line_edit_e)
        
        
        layout.addWidget(self.button)
        layout.addWidget(self.button1)
        layout.addWidget(self.warning)
        self.setLayout(layout)

    def create_CSV(self):
        file_name=self.line_edit_a.text()
        number_pages=int(self.line_edit_b.text())
        fp = int(self.line_edit_c.text())
        lp = int(self.line_edit_d.text())
        new_name=self.line_edit_e.text()
        createCSVS(file_name,fp,lp,new_name,number_pages)
        
    
    def analyze(self):
        new_name=self.line_edit_e.text()
        analyze("merged_"+new_name+".csv")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())



