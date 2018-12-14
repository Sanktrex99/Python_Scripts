#!/usr/bin/env python
#imports specific drivers from module
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#Takes input from user
user = input("Enter your UserId")
pass = input("Enter your Password")
url = input("Enter the address of site you want to use!!!")
button = input("Enter the name of button to be clicked.")
# If using Chrome!!
driver = webdriver.Chrome()

def site():
   driver.get(url)
   driver.find_element_by_id("login").send_keys(user)
   driver.find_element_by_id("pass").send_keys(pass)
   driver.find_element_by_id(button).click()
