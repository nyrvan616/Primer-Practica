from selenium import webdriver
from selenium_manager import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

driver = webdriver.Chrome(ChromeDriverManager().install())

#Abrir la pagina de selenium
driver.get("https://www.selenium.dev/")
driver.maximize_window()