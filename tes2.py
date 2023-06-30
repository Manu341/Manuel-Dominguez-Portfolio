import re
import csv
import pandas as pd
import locale
from PyQt5 import QtWidgets


def display_dictionary(data, parent=None):
    dialog = QtWidgets.QDialog(parent)
    table = QtWidgets.QTableWidget(dialog)
    table.setRowCount(len(data))
    table.setColumnCount(2)
    table.setHorizontalHeaderLabels(["Key", "Value"])

    for i, (key, value) in enumerate(data.items()):
        table.setItem(i, 0, QtWidgets.QTableWidgetItem(str(key)))
        table.setItem(i, 1, QtWidgets.QTableWidgetItem(str(value)))

    layout = QtWidgets.QVBoxLayout(dialog)
    layout.addWidget(table)
    dialog.exec_()

#path=input("Ingrese archivo: ")
def analyze(path):
    locale.setlocale(locale.LC_ALL, 'en_DK.UTF-8')
    id=dict()
    pattern=r"[0-9]"
    with open(path) as csvfile:
        reader=csv.DictReader(csvfile)
        for rows in reader:
            try:
                rows["CONCEPTO"]=re.sub(pattern,"",rows["CONCEPTO"])
                if rows["CONCEPTO"] not in id:
                    if rows["CREDITO"]!="":
                        id.setdefault(rows["CONCEPTO"],locale.atof(rows["CREDITO"]))
                    else:
                        id.setdefault(rows["CONCEPTO"],locale.atof(rows["DEBITO"]))
                else:
                    try:
                        if rows["CREDITO"]!="":
                            id[rows["CONCEPTO"]]+=locale.atof(rows["CREDITO"])
                        else:
                            id[rows["CONCEPTO"]]+=locale.atof(rows["DEBITO"])
                    except ValueError:
                        print("No hay ninguno con ese valor.")
            except ValueError:
                print("No hay valor")
    #ab=float(input("Saldo al final de la pagina: "))
    """ for keys,values in id.items():
    #    ab+=values
        print(keys,"----->",values) """
        
    dialog = QtWidgets.QDialog(parent=None)
    table = QtWidgets.QTableWidget(dialog)
    table.setRowCount(len(id))
    table.setColumnCount(2)
    table.setHorizontalHeaderLabels(["Key", "Value"])

    for i, (key, value) in enumerate(id.items()):
        table.setItem(i, 0, QtWidgets.QTableWidgetItem(str(key)))
        table.setItem(i, 1, QtWidgets.QTableWidgetItem(str(value)))
    
    layout = QtWidgets.QVBoxLayout(dialog)
    layout.addWidget(table)
    dialog.exec_()
    #print(ab)

