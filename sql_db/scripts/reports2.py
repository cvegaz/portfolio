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
    try:
        cursor.execute(sql_script)
        result = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        return pd.DataFrame(result, columns=columns)
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return pd.DataFrame()
    finally:
        cursor.close()

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

def get_past_tests_data(df, connection):
    matriculas = df['matricula'].tolist()
    query = f"""
    SELECT matricula, test_date, yds_40_1
    FROM physical_test
    WHERE matricula IN ({','.join(['%s'] * len(matriculas))})
    """
    cursor = connection.cursor()
    cursor.execute(query, tuple(matriculas))
    result = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    cursor.close()
    return pd.DataFrame(result, columns=columns)

def main():
    connection = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )

    df = execute_sql_script('sql/retrive.sql', connection)
    if not df.empty:
        save_to_excel(df, 'data/reporte.xlsx')
        plot_bar_chart(df, 'position', 'yds_40_1', 'data/reporte.png')

        past_tests_df = get_past_tests_data(df, connection)
        merged_df = pd.merge(df, past_tests_df, on='matricula', how='left', suffixes=('', '_past'))
        save_to_excel(merged_df, 'data/reporte2.xlsx')

    connection.close()

if __name__ == "__main__":
    main()