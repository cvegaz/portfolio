import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import os

load_dotenv()

def execute_sql_script(file_path, connection):
    with open(file_path, 'r') as file:
        sql_script = file.read()
    cursor = connection.cursor()
    cursor.execute(sql_script)
    
    result = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    cursor.close()
    return pd.DataFrame(result, columns=columns)

def save_to_excel(df, file_path):
    df.to_excel(file_path, index=False)

def plot_bar_chart(df, x_column, y_column, output_path):
    plt.figure(figsize=(10, 6))
    df.groupby(x_column)[y_column].mean().plot(kind='bar')
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.title(f'{y_column} by {x_column}')
    plt.savefig(output_path)
    plt.close()

def main():
    connection = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )

    df = execute_sql_script('sql/retrive.sql', connection)
    save_to_excel(df, 'data/reporte.xlsx')
    plot_bar_chart(df, 'position', 'yds_40_1', 'data/reporte.png')

    connection.close()

if __name__ == "__main__":
    main()