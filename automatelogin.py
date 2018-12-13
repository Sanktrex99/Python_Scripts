from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
def site():
   driver.get("http://172.16.1.11:1000/keepalive?0c0f0c0604030127")
   driver.find_element_by_id("login").send_keys("B218***")
   driver.find_element_by_id("pass").send_keys("***************")
   driver.find_element_by_id("Continue").click()
