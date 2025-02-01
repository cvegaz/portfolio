import os
import csv

#ejemplo de abrir un archivo CSV desde un path
#se especifica tipo de encoding para evitar conflicto de lectura de caracteres en los datos como acentos
csv_file_path = r'G:\Shared drives\2024 Juv CCM\2024 Juv\ONEFA\dataJuv24.csv'
with open(csv_file_path, 'r', encoding = 'utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Skip header row if it exists
        i=0
        for row in csvreader:
            curp = row[9]
            fechaNac = row[20]
            name = row[16]
            i = i +1
            print(f'{curp} {fechaNac} {name} {i}')
