import os
import csv

def rename_folders_from_csv(csv_file_path, base_path):
    with open(csv_file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Skip header row if it exists
        x= os.listdir(base_path)
        #print(len(x))
        for row in csvreader:
            folder_number = row[0]
            column3_data = row[5]
            column4_data = row[3]
            #print(folder_number, len(folder_number))
            for i in x:
                pos = i.find(' ')
                if folder_number == i[:pos] :
                    print(folder_number, i, i[:pos])
                    new_folder_name = f"{folder_number} {column3_data} {column4_data}"
                    old_folder_path = os.path.join(base_path, i)
                    new_folder_path = os.path.join(base_path, new_folder_name)
                    os.rename(old_folder_path, new_folder_path)
                    print(f"Renamed folder: {i} to {new_folder_name}")
                        
# Example usage
csv_file_path = r'C:\Users\Usuario\TecRegistros\data.csv'
base_path = r'C:\Users\Usuario\TecRegistros'

rename_folders_from_csv(csv_file_path, base_path)