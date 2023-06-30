#CREO LOS CSV CON LOS TITULOS CORRECTOS
#HAY QUE PONER A MANO LAS AREAS
import tabula
import csv
import pandas as pd
from PyQt5 import QtWidgets

class CoordinatesDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.line_edit = QtWidgets.QLineEdit(self)
        self.setFixedSize(350,350)
        self.setWindowTitle("Ingrese las 4 coordenadas separadas por comas.")
        self.button_box = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel, self)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.line_edit)
        layout.addWidget(self.button_box)
        
def table_of_areas(number_pags, parent=None):
    table = []
    for i in range(number_pags):
        dialog = CoordinatesDialog(parent)
        result = dialog.exec_()
        if result == QtWidgets.QDialog.Accepted:
            cords = dialog.line_edit.text().split(",")
            x1 = float(cords[0])
            x2 = float(cords[1])
            x3 = float(cords[2])
            x4 = float(cords[3])
            table.append([x1, x2, x3, x4])
    return table


unnamed_columns = ['Unnamed: 0', 'Unnamed: 1', 'Unnamed: 2']
#ELIMINO LOS UNNAMED ASI NO QUEDAN ESPACIOS EN BLANCO
def delete_columns(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        columns_to_delete = [index for index, column in enumerate(header) if column in unnamed_columns]
        columns_to_keep = [index for index in range(len(header)) if index not in columns_to_delete]

    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        data = [row for row in reader]

    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        #writer.writerow([header[index] for index in columns_to_keep])
        for row in data:
            writer.writerow([row[index] for index in columns_to_keep])

def createCSVS(file_path,fp,lp,new_file,number_pags):
    files=[]
    areas=table_of_areas(number_pags)
    tables2=[]
    f=0
    for i in range(fp,lp+1):
        tables=tabula.read_pdf(file_path,pages=i,area=areas[f])
        tables2.append(tables[0])
        f+=1
    i=1
    for df in tables2:
        df.to_csv(str(i)+new_file+".csv",index=False)
        files.append(str(i)+new_file+".csv")
        i+=1 
    
    for i in range(lp+1):
        try:
            delete_columns(str(i)+new_file+".csv")
        except FileNotFoundError:
            print("No se pudo eliminar")

    df_list = [pd.read_csv(f) for f in files]
    df = pd.concat(df_list)
    df.to_csv("merged_"+new_file+".csv", index=False)

