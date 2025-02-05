# 🏈 Borregos_FBA Project

## 📌 Introduction

As a data engineer, I embarked on a project to create a comprehensive database for a collegiate American football team. The primary goal was to consolidate nine years of accumulated data from various Excel files into a structured MySQL database. These files contained general information about the student-athletes, results from speed and strength tests, and biometric measurements.

---

## 🚨 Problem Statement.

The challenge was to manage and analyze a vast amount of data stored in disparate Excel files. The data included general student-athlete information, speed and strength test results, and biometric measurements. The objective was to create a robust database that could be easily updated and queried for insights.

---

## 🌎 Impact

By consolidating the data into a single database, we aimed to streamline data management and enable comprehensive analysis. This would facilitate better decision-making in player recruitment, performance evaluation, and future projections.

---

## 💡 Solution

I designed and implemented a MySQL database with tables tailored to store player information, physical test results, and biometric measurements. The database schema was designed to be flexible, allowing for future modifications and additions of important fields. Python scripts were developed to populate and update the tables, ensuring data integrity and consistency.

---

## 📂 Data Set

The dataset comprised:
- General information about the student-athletes (players.csv)
- Results from speed and strength tests (physical_tests.csv)
- Biometric measurements (biometrics.csv)

---

## ⚙️ Methodology

1️⃣ **Database Design:** Created a MySQL database with tables for player information, physical test results, and biometric measurements.  
2️⃣ **Data Ingestion:** Developed Python scripts to read data from Excel files and populate the database tables.  
3️⃣ **Data Update:** Implemented Python scripts to update the database tables with new data.  
4️⃣ **Query Execution:** Enabled the execution of any query to facilitate research and analysis of the data.  

---

## 🔍 Conclusions

🚀 One of the most valuable outcomes was the ability to profile the ideal player for each position, aiding in recruitment efforts to surpass established standards.  
📈 Additionally, we could identify top athletes and project their future performance within the team.  

---

## 📂 Project Structure
```
Borregos_FBA
├── .env
├── .gitignore
├── .vscode/
│   └── settings.json
├── data/
│   ├── biometrics.csv
│   ├── fba_lm.xlsx
│   ├── physical_tests.csv
│   ├── players.csv
│   ├── reporte.xlsx
│   └── reporte2.xlsx
├── demo_conn.session.sql
├── README.md
├── requirements.txt
├── scripts/
│   ├── insert_data.py
│   ├── reports.py
│   ├── reports2.py
│   └── update_data.py
└── sql/
    ├── create_tables.sql
    └── retrive.sql
```


## Future Work
Future efforts will focus on identifying relationships between test results and player performance, providing deeper insights into player development and team success.