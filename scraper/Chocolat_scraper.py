from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
import os
import re

chromedriver = "/home/mars/Desktop/Chocolate/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
actions = ActionChains(driver)

driver.get('http://flavorsofcacao.com/chocolate_database.html')

timeout = 20
try:
    WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, '//*[(@id = "spryregion1")]//table')))
except TimeoutException:
    print('Timed out waiting for page to load')
    driver.quit()

this_table = driver.find_elements_by_xpath('//*[(@id = "spryregion1")]//table')

text_file = open("data.txt", "w")
titles = [text_file.write(x.text) for x in this_table]
text_file.close()












