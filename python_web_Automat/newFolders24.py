import os
import csv

def create_folders_from_csv(csv_file_path, output_path):
    with open(csv_file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Skip header row if it exists

        for row in csvreader:
            # Assuming the CSV file has 2 columns, you can adjust the indices accordingly
            column1_data = row[0]

            folder_name = column1_data
            folder_path = os.path.join(output_path, folder_name)

            # Create the folder if it doesn't exist
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
                print(f"Created folder: {folder_path}")
            else:
                print(f"Folder already exists: {folder_path}")


csv_file_path = r'G:\Shared drives\2024 LM CCM\2024 LM\ONEFA\Registros\FolderNames.csv'
output_path = r'G:\Shared drives\2024 LM CCM\2024 LM\ONEFA\Registros'
create_folders_from_csv(csv_file_path, output_path)
