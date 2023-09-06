import datetime as dt
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

# Open Asana website
browser.get("https://app.asana.com")

# XPATH
field_username = '//*[@id="Login-appRoot"]/div/div[1]/div[2]/form/div[1]/div/div/input'
btn_username = '//*[@id="Login-appRoot"]/div/div[1]/div[2]/form/div[2]'
field_password = '//*[@id="Login-appRoot"]/div/div[1]/form/div[1]/div/input'
btn_password = '//*[@id="Login-appRoot"]/div/div[1]/form/div[2]'
btn_solicitation_ti = '//*[@id="asana_sidebar"]/div/div[2]/div[1]/div[2]/nav[2]/div/div/div[2]/div[2]/div[''1]/div/div/a/div[1]'
btn_create_task = '//*[@id="asana_main_page"]/div[2]/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div[1]'
field_type_morning = '//*[@id="highlightedCell"]/label'
btn_select_cell = '//*[@id="highlightedCell"]/div[4]'
btn_project_cascade = '//*[@id="highlightedCell"]/div[4]/div/div[1]'
btn_select_project = '//*[@id="lui_149"]/div/div/a[3]'
btn_select_details = '//*[@id="highlightedCell"]/div[4]/div/div[3]'
btn_date_menu = '//*[@id="asana_main_page"]/div[2]/div[2]/div/div/div/div[2]/article/div[2]/div[1]/div/div/div[3]/div/div[2]/div[2]/div/div/div/div[1]'
field_type_date = '//*[@id="due_date_input_id_select"]'
hoje = dt.date.today()
dia = str(hoje.day)
mes = str(hoje.month)
ano = str(hoje.year)

# Login
username = 'fabio.saruwataru@cragea.com.br'
password = '1@Cragea2021'


usrname = browser.find_element(by=By.XPATH, value=field_username)
usrname.send_keys(username)
browser.find_element(by=By.XPATH, value=btn_username).submit()
time.sleep(2)  # Aguardar load da tela de senha
pssword = browser.find_element(by=By.XPATH, value=field_password)
pssword.send_keys(password)
browser.find_element(by=By.XPATH, value=btn_password).click()

# Movimentação pela página
time.sleep(4)
browser.find_element(by=By.XPATH, value=btn_solicitation_ti).click()
# Criação de nova tarefa
time.sleep(3)

# Criação task Sábado
browser.find_element(by=By.XPATH, value=btn_create_task).click()
browser.find_element(by=By.XPATH, value=field_type_morning).send_keys('TROCA HD BKP DIARIO SÁBADO')
time.sleep(2)
browser.find_element(by=By.XPATH, value=btn_select_details).click()
time.sleep(2)
browser.find_element(by=By.XPATH, value=btn_date_menu).click()  # Selecionar campo de data
time.sleep(2)
browser.find_element(by=By.XPATH, value=field_type_date).send_keys(f"{dia}/{mes}/{ano}")  # Inserir data
time.sleep(2)
browser.find_element(by=By.XPATH, value=btn_project_cascade).click()
time.sleep(2)
browser.find_element(by=By.XPATH, value=btn_select_project).click()  # Alterar projeto
time.sleep(2)
'''
# Criação task de Segunda a Sexta
for i in range(5):
    browser.find_element(by=By.XPATH, value=btn_create_task).click() # Create task
    time.sleep(2)
    browser.find_element(by=By.XPATH, value=field_type_morning).send_keys('TROCA HD BKP DIARIO TARDE') # Type
    time.sleep(2)
    browser.find_element(by=By.XPATH, value=btn_create_task).click() # Create task
    time.sleep(2)
    browser.find_element(by=By.XPATH, value=field_type_morning).send_keys('TROCA HD BKP DIARIO MANHÃ') # Type
    time.sleep(2)
time.sleep(2)'''