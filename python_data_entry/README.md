# 🏈 Automating Student-Athlete Registration for ONEFA with Selenium WebDriver

## 📌 Introduction

As a data engineer, I am always looking for ways to optimize and automate repetitive processes. This project was developed to **automate the registration process for student-athletes** in the **ONEFA (Organización Nacional Estudiantil de Futbol Americano) league in Mexico**.  

By using **Selenium WebDriver**, I streamlined the **submission of player data** from a structured `.csv` file into an online registration form. Additionally, I built file management scripts to organize and properly name essential documents, such as **birth certificates, proof of studies, and player photos**.

---

## 🚨 Problem Statement

Before automation, registering players into the system was a **time-consuming manual task** that required:  

- Manually inputting student-athlete data into the web form.  
- Uploading multiple documents one by one.  
- Managing and renaming disorganized files across different folders.  

This inefficiency **increased the risk of errors**, slowed down the registration process, and made it difficult to track document submissions.
---

## 🎥 Demonstration Video

Watch the full automation process in action:  
[![Automation Process](https://img.youtube.com/vi/KIzI0PT7JfE/0.jpg)](https://www.youtube.com/watch?v=KIzI0PT7JfE)

---

## 🌎 Impact

By automating the registration and file management process, I was able to:  

✅ **Reduce the time spent per registration** from several hours to just a few minutes.  
✅ **Minimize human error** by ensuring accurate and consistent data entry.  
✅ **Standardize document organization**, making it easier to retrieve and verify files.  
✅ **Enhance the overall workflow efficiency**, allowing staff to focus on more critical tasks.  

---

## 💡 Solution

To solve this issue, I developed a **Python-based automation tool** using:  

🔹 **Selenium WebDriver** to interact with the registration webpage, fill out forms, and upload documents.  
🔹 **CSV processing** to extract player information dynamically.  
🔹 **Automated file renaming** to ensure all documents follow a structured naming convention.  
🔹 **Folder organization scripts** to categorize and maintain a well-structured file system.  

The automation follows this workflow:  

1️⃣ Load player data from a `.csv` file.  
2️⃣ Open the web registration form using Selenium WebDriver.  
3️⃣ Populate the form fields with the corresponding student-athlete data.  
4️⃣ Locate and upload the required documents.  
5️⃣ Submit the registration and log the process.  

---

## 📂 Repository Structure

This repository contains multiple Python scripts that handle different aspects of the automation:

- **`sendKeys.py`** – Automates data entry into the web form, checking if a student is already registered.  
- **`fileOnefaUp.py`**, **`onefaPicsUpdate.py`**, **`onup.py`**, **`upWeb.py`**, **`upWeb1.2.py`** – Handle the document upload process.  
- **`newFolders.py`**, **`newFolders24.py`**, **`renameFolders.py`** – Organize and rename student documents systematically.  
- **`openCSV.py`**, **`readFiles.py`** – Read and process `.csv` files containing player data.  
- **`chromedriver.exe`** – ChromeDriver executable required for Selenium WebDriver to function.  
- **`LICENSE.chromedriver`** – License file for ChromeDriver.  
- **`data.csv`**, **`LM24.csv`** – Sample CSV files used for data extraction.  

---

## 📊 Dataset

The **dataset used in this project** contains the following columns:  

 

---

## ⚙️ Methodology

I followed an **agile approach** to develop and optimize the automation:

1️⃣ **Exploratory Data Analysis (EDA)** – Analyzed registration trends and identified bottlenecks.  
2️⃣ **Web Scraping & Automation Testing** – Used Selenium to understand form structures and potential errors.  
3️⃣ **Script Development** – Built modular Python scripts for different aspects of automation.  
4️⃣ **Performance Optimization** – Reduced processing time and improved script efficiency.  
5️⃣ **Deployment & Maintenance** – Ensured scripts can run consistently with minimal supervision.  

---
🔍 **Conclusions
🚀 **The automation reduced registration time from minutes to seconds.
📂 **A structured folder and naming system improved file retrieval and tracking.
✅ **Selenium WebDriver proved to be an efficient tool for web-based automation.


