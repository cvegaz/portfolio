import mysql.connector
import pandas as pd
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

def update_data_from_csv(file_path, table_name, connection):
    cursor = connection.cursor()
    data = pd.read_csv(file_path)
    for index, row in data.iterrows():
        if table_name == 'data_player':
            # Convert date fields to the correct format
            date_of_birth = parse_date(row['date_of_birth'])
            date_of_entry = parse_date(row['date_of_entry'])
            sql = """
                INSERT INTO data_player (matricula, first_name, middle_name, last_name_paternal, last_name_maternal, date_of_birth, position, academic_program, date_of_entry, origin, curp)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE first_name=VALUES(first_name), middle_name=VALUES(middle_name), last_name_paternal=VALUES(last_name_paternal), last_name_maternal=VALUES(last_name_maternal), date_of_birth=VALUES(date_of_birth), position=VALUES(position), academic_program=VALUES(academic_program), date_of_entry=VALUES(date_of_entry), origin=VALUES(origin), curp=VALUES(curp)
            """
            values = (row['matricula'], row['first_name'], row['middle_name'], row['last_name_paternal'], row['last_name_maternal'], date_of_birth, row['position'], row['academic_program'], date_of_entry, row['origin'], row['curp'])
        elif table_name == 'physical_test':
            # Convert test_date to the correct format
            test_date = parse_date(row['test_date'])
            sql = """
                INSERT INTO physical_test (matricula, test_date, yds_10_1, yds_10_2, yds_40_1, yds_40_2, pro_rt, pro_lt, l_rt, l_lt, bj_1, bj_2, vj_1, vj_2, bp_1, bp_2, clean_1, clean_2, squat_1, squat_2)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE test_date=VALUES(test_date), yds_10_1=VALUES(yds_10_1), yds_10_2=VALUES(yds_10_2), yds_40_1=VALUES(yds_40_1), yds_40_2=VALUES(yds_40_2), pro_rt=VALUES(pro_rt), pro_lt=VALUES(pro_lt), l_rt=VALUES(l_rt), l_lt=VALUES(l_lt), bj_1=VALUES(bj_1), bj_2=VALUES(bj_2), vj_1=VALUES(vj_1), vj_2=VALUES(vj_2), bp_1=VALUES(bp_1), bp_2=VALUES(bp_2), clean_1=VALUES(clean_1), clean_2=VALUES(clean_2), squat_1=VALUES(squat_1), squat_2=VALUES(squat_2)
            """
            values = (
                row['matricula'], test_date, 
                float(row['yds_10_1']) if row['yds_10_1'] else None, 
                float(row['yds_10_2']) if row['yds_10_2'] else None, 
                float(row['yds_40_1']) if row['yds_40_1'] else None, 
                float(row['yds_40_2']) if row['yds_40_2'] else None, 
                float(row['pro_rt']) if row['pro_rt'] else None, 
                float(row['pro_lt']) if row['pro_lt'] else None, 
                float(row['l_rt']) if row['l_rt'] else None, 
                float(row['l_lt']) if row['l_lt'] else None, 
                float(row['bj_1']) if row['bj_1'] else None, 
                float(row['bj_2']) if row['bj_2'] else None, 
                float(row['vj_1']) if row['vj_1'] else None, 
                float(row['vj_2']) if row['vj_2'] else None, 
                float(row['bp_1']) if row['bp_1'] else None, 
                float(row['bp_2']) if row['bp_2'] else None, 
                float(row['clean_1']) if row['clean_1'] else None, 
                float(row['clean_2']) if row['clean_2'] else None, 
                float(row['squat_1']) if row['squat_1'] else None, 
                float(row['squat_2']) if row['squat_2'] else None
            )
        elif table_name == 'biometric':
            # Convert date to the correct format
            date = parse_date(row['date'])
            sql = """
                INSERT INTO biometric (matricula, date, height, weight, acl, mass, mme, bmi, pgc, aec_act, protein, minerals)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE date=VALUES(date), height=VALUES(height), weight=VALUES(weight), acl=VALUES(acl), mass=VALUES(mass), mme=VALUES(mme), bmi=VALUES(bmi), pgc=VALUES(pgc), aec_act=VALUES(aec_act), protein=VALUES(protein), minerals=VALUES(minerals)
            """
            values = (
                row['matricula'], date, 
                float(row['height']) if row['height'] else None, 
                float(row['weight']) if row['weight'] else None, 
                float(row['acl']) if row['acl'] else None, 
                float(row['mass']) if row['mass'] else None, 
                float(row['mme']) if row['mme'] else None, 
                float(row['bmi']) if row['bmi'] else None, 
                float(row['pgc']) if row['pgc'] else None, 
                float(row['aec_act']) if row['aec_act'] else None, 
                float(row['protein']) if row['protein'] else None, 
                float(row['minerals']) if row['minerals'] else None
            )
        cursor.execute(sql, values)
    connection.commit()
    cursor.close()

def main():
    connection = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME')
    )

    update_data_from_csv('data/players.csv', 'data_player', connection)
    update_data_from_csv('data/physical_tests.csv', 'physical_test', connection)
    update_data_from_csv('data/biometrics.csv', 'biometric', connection)

    connection.close()

if __name__ == "__main__":
    main()