from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time


ID = input("ID:  ")
PassWord = input("PassWord:  ")
twofa = input("Token:  ")


driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get("https://apps.ambev.com.br/logon/LogonPoint/tmindex.html")

driver.implicitly_wait(25)

#acessar elementos dentro do iframe driver.switch_to("iframe" )
#PyWinAuto para controle do APRJ

logar = driver.find_element(by=By.XPATH, value= "//a[@id='loginBtn']")
logar.click()

Usuário = driver.find_element(by=By.XPATH, value= "//input[@id='login']")
Usuário.send_keys(ID)

Credenciais = driver.find_element(by=By.XPATH, value= "//input[@id='passwd']")
Credenciais.send_keys(PassWord)

Submit = driver.find_element(by=By.XPATH, value= "//a[@id='loginBtn']")
Submit.click()

Token = driver.find_element(by=By.ID, value="passwd")
Token.send_keys(twofa)





