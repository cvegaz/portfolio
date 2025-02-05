import mysql.connector
import csv
from datetime import datetime
from dotenv import load_dotenv
import os
load_dotenv()
def parse_date(date_str):
    for fmt in ('%d-%m-%Y', '%d %m %Y'):
        try:
            return datetime.strptime(date_str, fmt).strftime('%Y-%m-%d')
        except ValueError:
            pass
    raise ValueError(f"No valid date format found for {date_str}")

def insert_data_from_csv():
    # Database connection
    conn = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )
    cursor = conn.cursor()

    # Insert players data
    with open('data/players.csv', mode='r', encoding='utf-8') as players_file:
        csv_reader = csv.reader(players_file)
        next(csv_reader)  # Skip header row
        for row in csv_reader:
            # Convert date fields to the correct format
            row[5] = parse_date(row[5])  # date_of_birth
            row[8] = parse_date(row[8])  # date_of_entry
            cursor.execute("""
                INSERT INTO data_player (matricula, first_name, middle_name, last_name_paternal, last_name_maternal, date_of_birth, position, academic_program, date_of_entry, origin, curp)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, row)

    # Insert physical tests data
    with open('data/physical_tests.csv', mode='r',encoding='utf-8') as tests_file:
        csv_reader = csv.reader(tests_file)
        next(csv_reader)  # Skip header row
        for row in csv_reader:
            # Convert test_date to the correct format
            row[1] = parse_date(row[1])  # test_date
              
            # Convert each element to the appropriate data type, leave empty if no value
            row = [
                row[0],  # matricula (string)
                row[1],  # test_date (string, already converted)
                float(row[2]) if row[2] else None,  # yds_10_1
                float(row[3]) if row[3] else None,  # yds_10_2
                float(row[4]) if row[4] else None,  # yds_40_1
                float(row[5]) if row[5] else None,  # yds_40_2
                float(row[6]) if row[6] else None,  # pro_rt
                float(row[7]) if row[7] else None,  # pro_lt
                float(row[8]) if row[8] else None,  # l_rt
                float(row[9]) if row[9] else None,  # l_lt
                float(row[10]) if row[10] else None,  # bj_1
                float(row[11]) if row[11] else None,  # bj_2
                float(row[12]) if row[12] else None,  # vj_1
                float(row[13]) if row[13] else None,  # vj_2
                float(row[14]) if row[14] else None,  # bp_1
                float(row[15]) if row[15] else None,  # bp_2
                float(row[16]) if row[16] else None,  # clean_1
                float(row[17]) if row[17] else None,  # clean_2
                float(row[18]) if row[18] else None,  # squat_1
                float(row[19]) if row[19] else None   # squat_2
            ]
            cursor.execute("""
                INSERT INTO physical_test (matricula, test_date, yds_10_1, yds_10_2, yds_40_1, yds_40_2, pro_rt, pro_lt, l_rt, l_lt, bj_1, bj_2, vj_1, vj_2, bp_1, bp_2, clean_1, clean_2, squat_1, squat_2)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, row)

    # Insert biometric data
    with open('data/biometrics.csv', mode='r',encoding='utf-8') as biometrics_file:
        csv_reader = csv.reader(biometrics_file)
        next(csv_reader)  # Skip header row
        for row in csv_reader:
            # Convert date to the correct format
            row[1] = parse_date(row[1])  # date
            
            # Convert each element to the appropriate data type, leave empty if no value
            row = [
                row[0],  # matricula (string)
                row[1],  # date (string, already converted)
                float(row[2]) if row[2] else None,  # height
                float(row[3]) if row[3] else None,  # weight
                float(row[4]) if row[4] else None,  # acl
                float(row[5]) if row[5] else None,  # mass
                float(row[6]) if row[6] else None,  # mme
                float(row[7]) if row[7] else None,  # bmi
                float(row[8]) if row[8] else None,  # pgc
                float(row[9]) if row[9] else None,  # aec_act
                float(row[10]) if row[10] else None,  # protein
                float(row[11]) if row[11] else None,  # minerals
            ]
            
            cursor.execute("""
                INSERT INTO biometric (matricula, date, height, weight, acl, mass, mme, bmi, pgc, aec_act, protein, minerals)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, row)

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    insert_data_from_csv()