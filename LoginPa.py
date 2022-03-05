from pyautogui import click
from pyodbc import drivers
from select import select
from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\chromedriver_win32 (1)\chromedriver.exe")

# Singup Page
driver.get("https://jt-dev.azurewebsites.net/#/SignUp")
driver.maximize_window()
time.sleep(1)

# element_lan = driver.find_element_by_name("language").click()

dropdown=driver.find_element_by_name("language").click()
time.sleep(3)
dropdown1=driver.find_element_by_xpath("//*[@id='ui-select-choices-row-1-0']/a/div").click()

time.sleep(2)

element_usename=driver.find_element_by_xpath("//input[@id='name']")
element_usename.send_keys("Ashwini Jadhav")
time.sleep(2)

element_org=driver.find_element_by_xpath("//input[@name='orgName']")
element_org.send_keys("IIFL pvt ltd")
time.sleep(2)

element_org=driver.find_element_by_xpath("//input[@name='email']")
element_org.send_keys("ashwiniljadhav4@gmail.com")
time.sleep(1)

driver.implicitly_wait(2)

box_ele=driver.find_element_by_xpath("//span[@class='black-color ng-binding']").click()
time.sleep(2)

sumbit = driver.find_element_by_xpath("//div[@class='form-group custom-form-group']").click()
time.sleep(2)

driver.getPageSource().contains("A welcome email has been sent. Please check your email.")
time.sleep(2)
#Close the driver

driver.close()





