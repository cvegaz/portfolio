from selenium import webdriver                  #hay que hacer uodate del selenium
from selenium.webdriver.common.by import By     #hay que descargar ultima versión de chromedriver.exe y colocarlo en la misma carpeta donde está corriendo nuestro archivo .py
from selenium.webdriver.support.ui import Select
import time
import csv

def addPic(driver):
    csv_file_path = r'G:\My Drive\Cursos\2023 Python\RegistrosONEFA\LM24.csv'
    pic_path = r'G:\Shared drives\2024 LM CCM\2024 LM\ONEFA\FOTOS REGISTROS\fotos_ONEFA'

    for i in range(80):                                     #revisar cuántos registros se quieren modificar
        xpath= f'//*[@id="dataTable"]/tbody/tr[{i+1}]/td[5]'                        
        registro = driver.find_element('xpath',xpath)
        jerseyR = int(registro.text)
        with open(csv_file_path, 'r', encoding = 'utf-8') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)  # Skip header row if it exists
            for row in csvreader:
                jerseycvs = int(row[0])
                name = row[5]
                if jerseycvs == jerseyR:
                    print(f'{jerseyR} {jerseycvs} {name}')
                    newPath=f'/html/body/div/div[2]/table/tbody/tr[{i+1}]/td[10]'
                    access = driver.find_element('xpath',newPath)
                    access.click()
                    #selectPic(name)
                    #save()
                    selectFile(name)
                    time.sleep(1)
                    goinit()
def goinit():
    initPath = f'//*[@id="navbarNav"]/ul/li[2]/a' # revisar el real!!!!
    access = driver.find_element('xpath',initPath)
    access.click()
    time.sleep(1)
    #da click sobre el equipo de 'Mayor' revisar!!!!!
    access = driver.find_element('xpath','/html/body/div/div[2]/div[2]/div/div')
    access.click()
def selectPic(pic):
    # pic debe tener un row[n] del .cvs donde está almacenado el "nombre de la foto" 
    picName = f'G:\\Shared drives\\2024 LM CCM\\2024 LM\\ONEFA\\FOTOS REGISTROS\\fotos_ONEFA\\{pic}.jpg'
    accessPic = driver.find_element('xpath','//*[@id="fotografia"]')
    accessPic.send_keys(picName)
    
def save():
    saveButt = driver.find_element('xpath','//*[@id="datos_jugador"]')
    saveButt.click()

def selectFile(name):
    # abre la pestaña para subir file de Comprobante de estudios
    accessCE = driver.find_element('xpath','//*[@id="historial-tab"]')
    accessCE.click()
    time.sleep(1)
    # path de tipo de documento: Comprobante de Etudios
    dropBox = driver.find_elements(by=By.TAG_NAME, value= 'Option')
    dropBox[5].click()      #por alguna razón se pone el valor 5, cuando en el html value es 4
    '''
    #por alguna razón esta manera no funciona
    dropBox = driver.find_element(By.ID, 'id_tipo')
    select = Select(dropBox)
    #select.select_by_visible_text("COMPROBANTE DE ESTUDIOS")
    select.select_by_value('4')
    time.sleep(2)
    '''
    #----------coloca el .pdf en el campo para seleccionarlo antes de guardar
    fileName = f'G:\\Shared drives\\2024 LM CCM\\2024 LM\\ONEFA\\FUA\\{name}.pdf'
    accessFile = driver.find_element('xpath','//*[@id="historial"]/form/div/div[2]/div/input')
    accessFile.send_keys(fileName)
    time.sleep(1)
    # path de boton de guardar
    accessSave = driver.find_element('xpath','//*[@id="docs_temp_jugador"]')
    accessSave.click()
    time.sleep(1)
    

#------INICIA EL PROGRAMA-------------    
# Entra a la pagina inicio
url = "https://www.onefa.mx/inicio.php"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
time.sleep(1)               # Espera un poco para que la página se cargue completamente
usuario = 'ccm'
psw = 'XXXX'
usuarioWeb = driver.find_element('xpath','//*[@id="usuario"]')
usuarioWeb.send_keys(usuario)
psWeb = driver.find_element('xpath','//*[@id="password"]')
psWeb.send_keys(psw)
access = driver.find_element('xpath','/html/body/div/div/div[2]/form/div[3]/div/div/input')
access.click()                             
time.sleep(1)
access = driver.find_element('xpath','/html/body/div/div[2]/div[2]/div/div')
access.click()  

addPic(driver)

time.sleep(1)
driver.quit()