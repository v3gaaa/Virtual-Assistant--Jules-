import eel
import pandas as pd
import os
import csv



@eel.expose
def agregar_aplicacion(x,y):
    list_data = [x, y]
    with open('programas.csv', 'a', newline='') as fd:
        csv_writer = csv.writer(fd)
        csv_writer.writerow(list_data)

    return "Aplicacion agregada correctamente"

