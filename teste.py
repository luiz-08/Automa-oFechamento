from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(executable_path='C:\Users\luizg\Desktop\AutoFechamento\chromedriver.exe')

teste = driver.find_element(by='By.ID')