from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

def addDataPlayer(driver):
    fechaWeb = driver.find_element('xpath','//*[@id="fec_nac"]')
    fechaWeb.send_keys(fechaNac)
    #time.sleep(1)
    #namesWeb = driver.find_element('xpath','//*[@id="nombre"]')
    #namesWeb.send_keys(name)
    #time.sleep(1)
    #lastNamesWeb = driver.find_element('xpath','//*[@id="apellido"]')
    #lastNamesWeb.send_keys(lastName)
    #time.sleep(1)
    accessPic = driver.find_element('xpath','//*[@id="fotografia"]')
    accessPic.send_keys(picName)
    time.sleep(1)
    jerseyWeb = driver.find_element('xpath','//*[@id="jersey"]')
    jerseyWeb.send_keys(jersey)
    dropBox = driver.find_elements(by=By.TAG_NAME, value= 'Option')
    dropBox[posONEFA].click()
    time.sleep(1)
    pesoWeb = driver.find_element('xpath','//*[@id="peso"]')
    pesoWeb.send_keys(peso)
    #time.sleep(1)
    estaturaWeb = driver.find_element('xpath','//*[@id="estatura"]')
    estaturaWeb.send_keys(estatura)
    #time.sleep(1)
    escuelaWeb = driver.find_element('xpath','//*[@id="escuela"]')
    escuelaWeb.send_keys(escuela)
    #time.sleep(1)
    nivelWeb = driver.find_element('xpath','//*[@id="nivel"]')
    nivelWeb.send_keys(nivel)
    #time.sleep(1)
    gradoWeb = driver.find_element('xpath','//*[@id="grado"]')
    gradoWeb.send_keys(grado)
    #time.sleep(1)
    matriculaWeb = driver.find_element('xpath','//*[@id="matricula"]')
    matriculaWeb.send_keys(matricula)
    #time.sleep(1)

def addNew(driver):
    CURPWeb = driver.find_element('xpath','//*[@id="curp"]')
    CURPWeb.send_keys(curp)
    accessPlayer = driver.find_element('xpath','/html/body/div/form/div/input[4]')
    accessPlayer.click()
    time.sleep(1)
    url = driver.current_url
    #print(url)
    if "curp" in url:
        #print('este alumno ya está registrado')
        elemento = driver.find_element('xpath','/html/body/div/div/p')
        
        if  "El jugador ya se encuentra en el equipo." in elemento.text:
            #print(f'{row[13]} {row[20]} {elemento.text}')
            print(f'{row[13]} {row[20]}')
            adDataButt = driver.find_element('xpath','/html/body/div/div/a[1]')
            adDataButt.click()
            addDataPlayer(driver)
            #------guardar ---------
            savePlayerButt = driver.find_element('xpath','//*[@id="guardar"]')
            savePlayerButt.click()
            time.sleep(2)
        
            addPlayer = driver.find_element('xpath','/html/body/div/div[1]/div[3]/div/a')
            addPlayer.click()
            time.sleep(1)
            #-------Fin Guardar -------
            '''
            initButt = driver.find_element('xpath','//*[@id="navbarNav"]/ul/li[2]/a')
            initButt.click()
            time.sleep(1)
            accessJuv = driver.find_element('xpath','/html/body/div/div[2]/div/div/div/a')
            accessJuv.click()
            time.sleep(1)
            addPlayer = driver.find_element('xpath','/html/body/div/div[1]/div[3]/div/a')
            addPlayer.click()
            time.sleep(1)
            '''
        elif "El jugador ya se encuentra en los registros y pertenece a otro equipo." in elemento.text:
            print(f'{row[13]} {row[20]} {elemento.text}')

            cancelButt = driver.find_element('xpath','/html/body/div/div/a[2]')
            cancelButt.click()
            time.sleep(1)
    elif "nuevo" in url:
        #print('ingresaremos los dato de un nuevo alumno')
        #print(f'{row[13]} {row[20]}')
        addDataPlayer(driver)
    
        #---------- guardamos jugador y regresamos a INICIO
        savePlayerButt = driver.find_element('xpath','//*[@id="guardar"]')
        savePlayerButt.click()
        time.sleep(2)
       
        addPlayer = driver.find_element('xpath','/html/body/div/div[1]/div[3]/div/a')
        addPlayer.click()
        time.sleep(1)
        #----------- hasta aquí se debió meter todos los faltantes haciendo GUARDAR------
        
        
        #---------- no guardaremos hasta estar seguros de que funciona --- regresamos a INICIO-----
  
        '''
        time.sleep(3)
        initButt = driver.find_element('xpath','//*[@id="navbarNav"]/ul/li[2]/a')
        initButt.click()
        time.sleep(1)
        accessJuv = driver.find_element('xpath','/html/body/div/div[2]/div/div/div/a')
        accessJuv.click()
        time.sleep(1)
        addPlayer = driver.find_element('xpath','/html/body/div/div[1]/div[3]/div/a')
        addPlayer.click()
        time.sleep(1)
        '''
        #----------- hasta aquí se debieron de meter todos los faltantes sin hacer guardar---------

    else:
        print('algo sucedió mal , check!!!')

url = "https://www.onefa.mx/inicio.php"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
time.sleep(1)


# Espera un poco para que la página se cargue completamente
usuario = 'CCM'
psw = 'XXXX'
usuarioWeb = driver.find_element('xpath','//*[@id="usuario"]')
usuarioWeb.send_keys(usuario)
psWeb = driver.find_element('xpath','//*[@id="password"]')
psWeb.send_keys(psw)
access = driver.find_element('xpath','/html/body/div/div/div[2]/form/div[3]/div/div/input')
access.click()                             
time.sleep(1)
accessJuv = driver.find_element('xpath','/html/body/div/div[2]/div/div/div/a')
accessJuv.click()
time.sleep(1)
addPlayer = driver.find_element('xpath','/html/body/div/div[1]/div[3]/div/a')
addPlayer.click()
time.sleep(1)
csv_file_path = r'I:\Shared drives\2024 Juv CCM\2024 Juv\ONEFA\testJuv.csv'
with open(csv_file_path, 'r', encoding = 'utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Skip header row if it exists
        
        for row in csvreader:
            curp = row[9]
            fechaNac = row[21]
            #print(f'{type(fechaNac)} {fechaNac}')
            #name = row[16]
            #lastName = row[17]
            picName = f'I:\\Shared drives\\2024 Juv CCM\\2024 Juv\\ONEFA\\FOTOS REGISTRO PRIMAVERA 2024\\{row[13]}.jpg'
            jersey = row[5]
            posONEFA = int(row[4])
            peso = row[19]
            estatura = row[18]
            escuela = 'TEC CCM'
            nivel = 'PREPA'
            grado = row[2]
            matricula = row[1]  
            addNew(driver)
      
time.sleep(3)
driver.quit()


#02-01-62007